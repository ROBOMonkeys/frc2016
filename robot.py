import wpilib as wpi
import util.config as config

from Subsystems import Shooter, Drive
from util.enums import XboxAxis, XboxButtons

class Myrobot(wpi.IterativeRobot):
    def robotInit(self):
        self.drive = Drive.RobotDrive()
        self.drive_type = config.SWERVE
    def teleopPeriodic(self):
        # drive.drive.drive.drive.drive()
        self.drive.drive(self.drive_type)

        ## to catch button presses
        # to shoot, press A
        if XboxButtons.A.poll():
            Shooter.shoot(8, 9)
        # to change drive types, press X
        if XboxButtons.X.poll():
            self.drive_type = int(not self.drive_type)

if __name__ == "__main__":
    wpi.run(Myrobot)
