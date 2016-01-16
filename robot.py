import wpilib as wpi

from Subsystems import Lifter, Shooter, Swerve

from enums import XboxAxis, XboxButtons, init_buttons


class Myrobot(wpi.IterativeRobot):
    def robotInit(self):
        self.contr = wpi.Joystick(0)
        init_buttons(self.contr)
        self.drive = swerve.traindrive              #will fix later


