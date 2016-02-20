from wpilib import AnalogInput, VictorSP, Joystick, Solenoid, AnalogGyro
from util.enums import init_buttons

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
encoders = [AnalogInput(0),
#            AnalogInput(1),
            AnalogInput(2),
            AnalogInput(3)]

enc_rel = 0
enc_abs = 0

enc_high = 0

#shoot_sole = Solenoid(0, 1)

# driving motors and steering motors setup
for i in range(4):
    driving_motors.append(VictorSP(i))
    steering_motors.append(VictorSP(i + 4))
#    encoders[i].reset()
#    encoders[i].setExternalDirectionMode()
#    encoders[i].setUpdateWhenEmpty()
#    encoders[i].setSamplesToAverage(12)

init_buttons(controller)

gyro.calibrate()
gyro.reset()

