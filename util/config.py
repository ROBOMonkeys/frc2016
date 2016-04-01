from wpilib import VictorSP, Joystick, Solenoid
from util.enums import init_buttons

SWERVE = 0
TANK = 1

LOGGING = False

controller = Joystick(0)
driving_motors = []
steering_motors = []
gate_mtr = VictorSP(5)
auto_state = 0


encoders = None

enc_ratio = 0.8692153

drop_sole = None 
shoot_sole = None

# driving motors and steering motors setup
for i in range(4):
    driving_motors.append(VictorSP(i))
#    steering_motors.append(VictorSP(i + 4))

init_buttons(controller)


