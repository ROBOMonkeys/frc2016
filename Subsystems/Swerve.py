from wpilib import VictorSP

class SwerveDrive():
    def __init__(self):
        self.m0 = VictorSP(0)
        self.m1 = VictorSP(1)
        self.m2 = VictorSP(2)
        self.m3 = VictorSP(3)

    def drive(self, speed, contr):
        # do some drive bullshit here plz
        self.drive_motors = config.drive_motors
        self.steering_motors = config.steering_motors
        self.encoder = config.encoder

        self.reversed = False

        speed = self.drive_joy.GetMagnitude()
        angle = self.drive_joy.GetDirectionDegrees()

        pos = self.encoder.Get()

        # Limits the travel to -90 - 90 and reverses the motor
        if angle > 90:
            angle -= 180
            self.reversed = True
        elif angle < -90:
            angle += 180
            self.reversed = True
        else:
            self.reversed = False

        if self.reversed:
            speed = -speed

        turn_speed = (angle - pos) / 180 + .01

        # Limit the turning to -90 - 90 just in case
        if self.encoder.Get() < - 90 and turn_speed < 0:
            turn_speed = 0
        elif self.encoder.Get() > 90 and turn_speed > 0:
            turn_speed = 0

        # This will still let it turn at full speed
        if self.hs_button.get():
            speed /= 2

        # This will cut everything in half
        if self.hs_steer_button.get():
            speed /= 2
            turn_speed /= 2

        # Acutally set the motors
        for i in self.drive_motors:
            i.Set(speed)
        for i in self.steering_motors:
            i.Set(speed)
        #we will look and edit all of this later
