from wpilib import Encoder, VictorSP, Joystick, Solenoid, AnalogGyro
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
encoders = [Encoder(0, reverseDirection=True),
            Encoder(2, reverseDirection=True),
            Encoder(4, reverseDirection=True),
            Encoder(6, reverseDirection=True)]

#drop_sole = Solenoid(0, 1)

# driving motors and steering motors setup
for i in range(4):
    driving_motors.append(VictorSP(i))
    steering_motors.append(VictorSP(i + 4))
    encoders[i].reset()
#    encoders[i].setExternalDirectionMode()
#    encoders[i].setUpdateWhenEmpty()
#    encoders[i].setSamplesToAverage(12)

init_buttons(controller)

gyro.calibrate()
gyro.reset()

