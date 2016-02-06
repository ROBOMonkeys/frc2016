import wpilib as wpi
import util.config as config

from Subsystems import Lifter, Shooter, Swerve
from enums import XboxAxis, XboxButtons, init_buttons

class Myrobot(wpi.IterativeRobot):
    def robotInit(self):
        self.contr = config.controller
        init_buttons(self.contr)
        self.drive = Swerve.SwerveDrive()


    def teleopPeriodic(self):
##        self.y = self.contr.getRawAxis(XboxAxis.R_Y)   # gets the y value from the right stick on the controller
##        self.x = self.contr.getRawAxis(XboxAxis.R_X)   # gets the x value from the right stick on the controller
##        self.rot = self.contr.getRawAxis(XboxAxis.L_X) # gets the x value from the left stick on the controller
##
##        # these if statements allow for a dead area in the controller
##        #  that way the robot won't move by itself when the sticks aren't being touched
##        if self.x < 0.25 and self.x > -0.25:
##            self.x = 0
##        if self.rot < 0.25 and self.rot > -0.25:
##            self.rot = 0
##        if self.y < 0.25 and self.y > -0.25:
##            self.y = 0

        self.drive.drive()

        if XboxButtons.A.poll():
            Shooter.shoot()
        if XboxButtons.X.poll():
            self.drive.default()

if __name__ == "__main__":
    wpi.run(Myrobot)
