from wpilib import Encoder, VictorSP, Joystick, Solenoid

driving_motors = []
steering_motors = []
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

# solenoid setup
drop_sole = Solenoid(0, 1)
