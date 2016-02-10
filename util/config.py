from wpilib import Encoder, VictorSP, Joystick, Solenoid, AnalogGyro
from util.enums import init_buttons

SWERVE = 0
TANK = 1

driving_motors = []
steering_motors = []
shoot_mtr = VictorSP(8)
suck_mtr = VictorSP(9)
gyro = AnalogGyro(1)
encoders = [Encoder(0, 1),
            Encoder(2, 3),
            Encoder(4, 5),
            Encoder(6, 7)]

# driving motors and steering motors setup
for i in range(4):
    driving_motors.append(VictorSP(i))
    steering_motors.append(VictorSP(i + 4))
    encoders[i].reset()

controller = Joystick(0)
init_buttons(controller)
gyro.reset()
# solenoid setup
#drop_sole = Solenoid(0, 1)
