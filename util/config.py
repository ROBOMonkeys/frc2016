from wpilib import Encoder, VictorSP, Joystick

driving_motors = []
steering_motors = []

# driving motors and steering motors setup
for i in range(4):
    driving_motors.append(VictorSP(i))
    steering_motors.append(VictorSP(i + 4))

encoder = Encoder(0, 1)

controller = Joystick(0)
