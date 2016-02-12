import wpilib
import util.config as config
import util.logging as logging
from util.enums import XboxAxis

class RobotDrive():
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
            while not pos < 10 or not pos > -10:
                mtr.set(spd)
                if pos > orig_pos:
                    spd = -spd
                pos = enc.get()

    def swerve(self):
        self.steering_motors = config.steering_motors
        
        x_speed = -self.contr.getRawAxis(XboxAxis.R_Y)
        rot = self.contr.getRawAxis(XboxAxis.L_X)

        # deadband zone
        if x_speed < 0.25 and x_speed > -0.25:
            x_speed = 0
        if rot < 0.25 and rot > -0.25:
            rot = 0

        s = []
        ts = []

        for enc in config.encoders:
            sp, tsp = self.swerve_determine_angle(x_speed * .75,
                                                  rot * 180,
                                                  enc)
            s.append(sp)
            ts.append(tsp)

        # Acutally set the motors
        for i in self.drive_motors:
            for spd in s:
                i.set(spd)
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

        return (speed, turn_speed)

    def tank(self):
        r = -self.contr.getRawAxis(XboxAxis.R_Y)
        l = -self.contr.getRawAxis(XboxAxis.L_Y)

        # deadband
        if r < 0.25 and r > -0.25:
            r = 0
        if l < 0.25 and l > -0.25:
            l = 0

        # set the wheels back straight
        self.default()

        # SET LEFT MOTORS
        self.drive_motors[0].set(l * 0.75)
        self.drive_motors[2].set(l * 0.75)

        # SET RIGHT MOTORS
        self.drive_motors[1].set(r * 0.75)
        self.drive_motors[3].set(r * 0.75)
    
    def drive(self, type):
        self.contr = config.controller
        self.drive_motors = config.driving_motors

        # gets information about the encoders so we can print it to the Driver station
        enc_str = [str(config.encoders[x].get()) for x in range(len(config.encoders))]
        logging.write_log(enc_str)
        
        if type == config.SWERVE:
            self.swerve()
        elif type == config.TANK:
            self.tank()
