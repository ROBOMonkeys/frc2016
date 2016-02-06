from threading import Timer

def shoot(sht_mtrs, piston):
    sht_mtrs.spin_up() # or, you know, whatever function to start them
    shoot_timer = Timer(0.5, real_shoot, (sht_mtrs, piston))
    shoot_timer.start()

def real_shoot(m, p):
    p.set() # or whatever function to make the piston fire
    m.set() # or whatever function to make the motors stop


