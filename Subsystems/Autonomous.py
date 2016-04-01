import util.config as config

from threading import Timer

def init_arm():
    x = Timer(0.5, lambda: stop_arm())
    x.start()
    config.gate_mtr.set(.3)

def move_forward():
    # LEFT MOTORS
    config.driving_motors[0].set(.75)
    config.driving_motors[2].set(.75)

    # RIGHT MOTORS
    config.driving_motors[1].set(-.75)
    config.driving_motors[3].set(-.75)

def move_backward():
    config.auto_state += 1
    # LEFT MOTORS
    config.driving_motors[0].set(-.75)
    config.driving_motors[2].set(-.75)

    # RIGHT MOTORS
    config.driving_motors[1].set(.75)
    config.driving_motors[3].set(.75)    

def stop():
    config.auto_state += 1
    for i in config.driving_motors:
        i.set(0)

def stop_arm():
    config.gate_mtr.set(0)
