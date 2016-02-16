from wpilib import DriverStation
import util.config as config

def write_log(s):
    if config.LOGGING:
        DriverStation.reportError(str(s) + "\n", False)
