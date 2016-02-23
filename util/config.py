from wpilib import VictorSP, Joystick, Solenoid, AnalogGyro
from util.enums import init_buttons
#from util.AnalogEncoder import AnalogEncoder

SWERVE = 0
TANK = 1

LOGGING = False

controller = Joystick(0)
driving_motors = []
steering_motors = []
shoot_mtr = VictorSP(8)
suck_mtr = VictorSP(9)
auto_state = 0
gyro = AnalogGyro(1)

encoders = None

drop_sole = None 
shoot_sole = None

# driving motors and steering motors setup
for i in range(4):
    driving_motors.append(VictorSP(i))
    steering_motors.append(VictorSP(i + 4))

gyro.calibrate()
gyro.reset()

init_buttons(controller)


