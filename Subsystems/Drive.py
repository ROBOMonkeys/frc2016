import util.config as config
import util.logging as logging
from util.enums import XboxAxis
from math import copysign
from wpilib.timer import Timer

class RobotDrive():
    def __init__(self):
        self.enc_seek = 0
        self.max = self.seek_to(90)
        self.min = -self.max

    def seek_to(self, deg):
        return deg * config.enc_ratio

    def get_speed(self, deg):
        return (0.00022575758 * (deg ** 2)) - \
            (0.0196993939 * deg) + \
            0.9741636364
        
    def new_new_swerve(self):
#        if thr is None:
        throttle = -config.controller.getRawAxis(XboxAxis.R_Y)
#        else:
#            throttle = thr

#        if rot is None:
        rot = config.controller.getRawAxis(XboxAxis.L_X)
#        else:
#            self.enc_seek = rot

        # deadband zone
        if throttle < 0.25 and throttle > -0.25:
            throttle = 0
        if rot < 0.25 and rot > -0.25:
            rot = 0

        self.enc_seek += rot

        if self.enc_seek > self.max:
            self.enc_seek = self.max
        elif self.enc_seek < self.min:
            self.enc_seek = self.min

        for enc in range(4):
            dist = config.encoders[enc].get()
            t_spd = 0.2
            spd = self.get_speed(self.enc_seek) * throttle

            # while the current encoder value is not within the dead zone
            #  we "seek" the motors to go to the value 
            while dist < self.enc_seek - 5 or \
                  dist > self.enc_seek + 5:
                
                if self.enc_seek < dist: # seeking to the left
                    if enc > 2:
                        config.steering_motors[enc].set(-t_spd)
                    else:
                        config.steering_motors[enc].set(t_spd)

                    if enc % 2 == 0:
                        config.driving_motors[enc].set(spd)
                        
                else: # seeking to the right
                    if enc > 2:
                        config.steering_motors[enc].set(t_spd)
                    else:
                        config.steering_motors[enc].set(-t_spd)

                    if enc % 2 != 0:
                        config.driving_motors[enc].set(spd)
                        


    def new_swerve(self):
        throttle = -config.controller.getRawAxis(XboxAxis.R_Y)
        rot = config.controller.getRawAxis(XboxAxis.L_X)

        # deadband zone
        if throttle < 0.25 and throttle > -0.25:
            throttle = 0
        if rot < 0.25 and rot > -0.25:
            rot = 0

        logging.write_log([self.enc_seek, rot])
            
        self.enc_seek += rot * 10

        inverse = False
        stop = False
        
        t = Timer()
        t.start()
        for m in range(len(config.steering_motors)):
            t.reset()
            logging.write_log("Turning")
            while (not config.encoders[m].get() < self.enc_seek + 15 or \
                   not config.encoders[m].get() > self.enc_seek - 15) and \
                not stop:
                if not inverse:
                    config.steering_motors[m].set((1 * -copysign(1, rot)) *
                                                  (self.enc_seek - config.encoders[m].get()))
                                                  
                else:
                    config.steering_motors[m].set((1 * copysign(1, rot)) *
                                                  (config.encoders[m].get() - self.enc_seek))
                logging.write_log(config.encoders[m].get())
                if t.hasPeriodPassed(1.5):
                    inverse = True
                    stop = True
                    break
            config.steering_motors[m].set(0)

        t.stop()
    
        for i in range(len(config.driving_motors)):
            if (i % 2):
                config.driving_motors[i].set(throttle)
            else:
                config.driving_motors[i].set(-throttle)
    
    def default(self):
        """
        Method to set wheels all to the same position
        """
        for i in range(len(config.encoders)):
            enc = config.encoders[i]
            mtr = config.steering_motors[i]
            orig_pos = enc.get()
            spd = .75
            pos = enc.get()
            while not pos > -10 and not pos < 10:
                mtr.set(spd)
                if pos > orig_pos:
                    spd = -spd
                pos = enc.get()

    def swerve(self):
        self.steering_motors = config.steering_motors
        
        x_speed = -config.controller.getRawAxis(XboxAxis.R_Y)
        rot = config.controller.getRawAxis(XboxAxis.L_X)

        # deadband zone
        if x_speed < 0.25 and x_speed > -0.25:
            x_speed = 0
        if rot < 0.25 and rot > -0.25:
            rot = 0

        s = []
        ts = []

        for enc in config.encoders:
            sp, tsp = self.swerve_determine_angle(x_speed * .75,
                                                  rot,
                                                  enc)
            s.append(sp)
            ts.append(tsp)

        # Acutally set the motors
        for i in range(len(config.driving_motors)):
            for spd in s:
                if (i % 2):
                    config.driving_motors[i].set(spd)
                else:
                    config.driving_motors[i].set(-spd)
        for i in self.steering_motors:
            for t_spd in ts:
                i.set(t_spd)
                
    def swerve_determine_angle(self, speed, angle, enc):
        pos = enc.get()
        reversed = False

        # Limits the travel to -90 - 90 and reverses the motor
        if angle > 180:
##            angle -= 180
            reversed = True
        elif angle < -180:
##            angle += 180
            reversed = True
        else:
            reversed = False

        if reversed:
            speed = -speed

        turn_speed = (angle - pos) / 180 + .01

        # Limit the turning to -90 - 90 just in case
        if enc.get() < - 180 and turn_speed < 0:
            turn_speed = 0
        elif enc.get() > 180 and turn_speed > 0:
            turn_speed = 0

        return (speed, angle)

    def tank(self):
        r = -config.controller.getRawAxis(XboxAxis.R_Y)
        l = -config.controller.getRawAxis(XboxAxis.L_Y)

        # deadband
        if r < 0.25 and r > -0.25:
            r = 0
        if l < 0.25 and l > -0.25:
            l = 0

        # set the wheels back straight
        self.default()

        # SET LEFT MOTORS
        config.driving_motors[0].set(l * 0.75)
        config.driving_motors[2].set(l * 0.75)

        # SET RIGHT MOTORS
        config.driving_motors[1].set(r * 0.75)
        config.driving_motors[3].set(r * 0.75)
    
    def drive(self, type):
        # gets information about the encoders so we can print it to the Driver station
#        logging.write_log([enc.getDirection() for enc in config.encoders])
        
        if type == config.SWERVE:
            self.new_new_swerve()
        elif type == config.TANK:
            self.tank()
