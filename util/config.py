from wpilib import DigitalInput, VictorSP, Joystick, Solenoid, AnalogGyro
from util.enums import init_buttons

SWERVE = 0
TANK = 1

controller = Joystick(0)
driving_motors = []
steering_motors = []
shoot_mtr = VictorSP(8)
suck_mtr = VictorSP(9)
gyro = AnalogGyro(1)
#encoders = [Encoder(aChannel=0, bChannel=1, reverseDirection=True),
#            Encoder(aChannel=2, bChannel=3, reverseDirection=True),
#            Encoder(aChannel=4, bChannel=5, reverseDirection=True),
#            Encoder(aChannel=6, bChannel=7, reverseDirection=True)]
encoders = [DigitalInput(0),
            DigitalInput(1)]
#drop_sole = Solenoid(0, 1)

# driving motors and steering motors setup
for i in range(4):
    driving_motors.append(VictorSP(i))
    steering_motors.append(VictorSP(i + 4))
#    encoders[i].reset()

init_buttons(controller)

gyro.calibrate()
gyro.reset()

