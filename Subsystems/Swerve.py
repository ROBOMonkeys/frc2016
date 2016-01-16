from wpilib import VictorSP

class SwerveDrive():
    def __init__(self):
        self.m0 = VictorSP(0)
        self.m1 = VictorSP(1)
        self.m2 = VictorSP(2)
        self.m3 = VictorSP(3)

    def drive(self, speed):
        # do some drive bullshit here plz
