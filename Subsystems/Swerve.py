import util.config as config
from enums import XboxAxis

class SwerveDrive():
    def default(self):
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
    
    def determine_angle(self, speed, angle, enc):
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
    
    def drive(self):
        # do some drive bullshit here plz
        self.contr = config.controller
        self.drive_motors = config.driving_motors
        self.steering_motors = config.steering_motors

#        speed = self.contr.getMagnitude()
#        angle = self.contr.getDirectionDegrees()

        x = self.contr.getRawAxis(XboxAxis.L_Y)
        rot = self.contr.getRawAxis(XboxAxis.R_X)

        if x < 0.25 and x > -0.25:
            x = 0
        if rot < 0.25 and rot > -0.25:
            rot = 0

        s = []
        ts = []

        for enc in config.encoders:
            sp, tsp = self.determine_angle(x * .75,
                                           rot * 180,
                                           enc)
            s.append(sp)
            ts.append(tsp)

        # This will still let it turn at full speed
#        if self.hs_button.get():
#            speed /= 2

        # This will cut everything in half
#        if self.hs_steer_button.get():
#            speed /= 2
#            turn_speed /= 2

        # Acutally set the motors
        for i in self.drive_motors:
            for spd in s:
                i.set(spd)
        for i in self.steering_motors:
            for t_spd in ts:
                i.set(t_spd)
        #we will look and edit all of this later
