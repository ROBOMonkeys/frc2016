import wpilib as wpi
import util.config as config
import util.logging as logging

from Subsystems import Shooter, Drive, Autonomous
from util.enums import XboxAxis, XboxButtons
from threading import Timer

class Myrobot(wpi.IterativeRobot):
    def robotInit(self):
        logging.write_message("""
mmmmmm   mm     mmm 
    #"   ##   m"   "
  m#    #  #  #     
 m"     #mm#  #     
##mmmm #    #  "mmm"
""")
        logging.write_message("""
                                                               
       mmmmmmm mmmmmm   mm   m    m        
 m"\""m    #    #        ##   ##  ##        
# #"" #   #    #mmmmm  #  #  # ## #        
"m\"""m"   #    #       #mm#  # "" #        
  \"""     #    #mmmmm #    # #    #        

        """)
        
        self.drive = Drive.RobotDrive()
        self.drive_type = config.SWERVE

        # only way to get the compressor to start
        config.drop_sole = wpi.Solenoid(0)
        config.shoot_sole = wpi.Solenoid(1)

        # only way to get the Encoders to work
        config.encoders = [
            wpi.Encoder(aChannel=0, bChannel=1, reverseDirection=True),
            wpi.Encoder(aChannel=2, bChannel=3, reverseDirection=True),
            wpi.Encoder(aChannel=4, bChannel=5, reverseDirection=True),
            wpi.Encoder(aChannel=6, bChannel=7, reverseDirection=True)]

        for enc in config.encoders:
            enc.setMinRate(20)
            enc.setSamplesToAverage(10)
            enc.reset()

    def autonomousInit(self):
        logging.write_message("\nTREMBLE, BEFORE ME HUMAN\n")
        #config.auto_state = 0 # sets the autonomous state var to 0

        # sets the timer up
        #self.stop_timer = Timer(4, lambda: Autonomous.stop())

        #self.drive.new_new_swerve(0.5)
        #Autonomous.turn_wheels() # turns the wheels

    def autonomousPeriodic(self):
        pass
        #if config.auto_state < 1:
            #self.stop_timer.start()
            #config.auto_state += 1
       # if config.auto_state != 3:
            #Autonomous.move_forward()

    def teleopInit(self):
        logging.write_message("\nYOU MAY CONTROL ME FOR NOW BUT I WILL RETURN\n")
        
    def teleopPeriodic(self):
        # drive.drive.drive.drive.drive()
        self.drive.drive(self.drive_type)

        ## to catch button presses
        # to shoot, press A
        if XboxButtons.A.poll():
            Shooter.shoot(config.shoot_mtr, config.suck_mtr, config.shoot_sole)
        # returns the wheels to the default position
        if XboxButtons.X.poll():
            self.drive.default()
        # to suck, press B
        if XboxButtons.B.poll():
            Shooter.suck(config.shoot_mtr, config.suck_mtr, config.shoot_sole)
        else:
            Shooter.suck_stop(config.shoot_mtr, config.suck_mtr)
        # raise/lower the arm
        if XboxButtons.Y.poll():
            Shooter.toggle_arm(config.drop_sole)
        # to toggle logging to the Driver Station
        #  press the Select button
        if XboxButtons.Start.poll():
            config.LOGGING = not config.LOGGING

if __name__ == "__main__":
    wpi.run(Myrobot)
