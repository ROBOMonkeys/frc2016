from threading import Timer

def shoot(sht_mtrs, piston):
    sht_mtrs.set(-.8) # or, you know, whatever function to start them
    shoot_timer = Timer(0.5, real_shoot, (sht_mtrs, piston))
    shoot_timer.start()

def real_shoot(m, p):
    p.set(True) # or whatever function to make the piston fire
    m.set(0) # or whatever function to make the motors stop

def suck(sht_mtrs, suck_mtrs, piston):
    sht_mtrs.set(.8)
    suck_mtrs.set(.8)
    piston.set(False)

def suck_stop(sht_mtrs, suck_mtrs)
    sht_mtrs.set(0)
    suck_mtrs.set(0)
