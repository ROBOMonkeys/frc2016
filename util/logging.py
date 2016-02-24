from wpilib import DriverStation
import util.config as config

def write_log(s):
    if config.LOGGING and \
       s is not None:
        DriverStation.reportError(str(s) + "\n", False)

def write_message(s):
    DriverStation.reportError(str(s) + "\n", False)
