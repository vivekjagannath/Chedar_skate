import dxl
import time
a = dxl.get_available_ports()
d = dxl.dxl(a[0], 1000000)
d.set_speed({i: 200 for i in range(1,13)})
d.set_goal_position({i: 512 for i in range(1,13)})
time.sleep(2)
while True: 
    d.set_goal_position({1: 512, 2: 461, 3: 448, 4: 512, 5: 562, 6: 575, 7: 512, 8: 574, 9: 384, 10: 512, 11: 574, 12: 384})
    time.sleep(0.8)
    d.set_goal_position({1: 512, 2: 696, 3: 448, 4: 512, 5: 327, 6: 575, 7: 512, 8: 515, 9: 431, 10: 512, 11: 515, 12: 431})
    time.sleep(0.8)