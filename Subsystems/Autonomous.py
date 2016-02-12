import util.config as config

from threading import Timer

def turn_wheels():
    x = Timer(1, lambda: stop())
    x.start()
    for i in config.steering_motors:
        i.set(.25)

def move_forward():
    for i in config.driving_motors:
        if i.get() == 0:
            i.set(0.25)

def stop():
    config.auto_state += 1
    for i in config.steering_motors:
        i.set(0)
    for i in config.driving_motors:
        i.set(0)
