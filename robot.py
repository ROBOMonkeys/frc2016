import wpilib as wpi
import util.config as config

from Subsystems import Shooter, Drive, Autonomous
from util.enums import XboxAxis, XboxButtons
from threading import Timer

class Myrobot(wpi.IterativeRobot):
    def robotInit(self):
        self.drive = Drive.RobotDrive()
        self.drive_type = config.SWERVE

    def autonomousInit(self):
        config.auto_state = 0 # sets the autonomous state var to 0

        # sets the timer up
        self.stop_timer = Timer(4, lambda: Autonomous.stop())

        Autonomous.turn_wheels() # turns the wheels

    def autonomousPeriodic(self):
        if config.auto_state < 1:
            self.stop_timer.start()
            config.auto_state += 1
        if config.auto_state != 3:
            Autonomous.move_forward()
        
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
