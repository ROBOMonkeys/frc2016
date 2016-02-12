from wpilib import Encoder, VictorSP, Joystick, Solenoid, AnalogGyro
from util.enums import init_buttons

SWERVE = 0
TANK = 1

controller = Joystick(0)
driving_motors = []
steering_motors = []
shoot_mtr = VictorSP(8)
suck_mtr = VictorSP(9)
auto_state = 0
gyro = AnalogGyro(1)
encoders = [Encoder(0, 1),
            Encoder(2, 3),
            Encoder(4, 5),
            Encoder(6, 7)]
#encoders = [DigitalInput(0),
#            DigitalInput(1)]

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

