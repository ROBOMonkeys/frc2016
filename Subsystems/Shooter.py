from threading import Timer

def shoot(sht_mtrs, o_mtr, piston):
    sht_mtrs.set(-1) # or, you know, whatever function to start them
    o_mtr.set(1)
    shoot_timer = Timer(1, real_shoot, (sht_mtrs, o_mtr, piston))
    shoot_timer.start()

def real_shoot(m, o_m, p):
    p.set(False) # or whatever function to make the piston fire
    m.set(0) # or whatever function to make the motors stop
    o_m.set(0)

def toggle_arm(p):
    p.set(not p.get())

def suck(sht_mtrs, suck_mtrs, piston):
    sht_mtrs.set(.8)
    suck_mtrs.set(-.8)
    piston.set(False)

def suck_stop(sht_mtrs, suck_mtrs):
    sht_mtrs.set(0)
    suck_mtrs.set(0)
