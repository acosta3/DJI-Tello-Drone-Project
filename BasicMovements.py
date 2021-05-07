from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())
me.takeoff()
me.send_rc_control(0,35,0,0) # moving forawr
sleep(2)
me.send_rc_control(0,0,0,0) # stop completely
me.land()

