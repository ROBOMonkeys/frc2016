from wpilib import DriverStation

def write_log(s):
    DriverStation.reportError(str(s) + "\n", False)
