import dxl
import time
a = dxl.get_available_ports()
d = dxl.dxl(a[0], 1000000)
d.set_goal_position({i:512 for i in range(1,13)})
time.sleep(2)
d.set_speed({i:800 for i in range(7,13)})
d.set_goal_position({7: 512, 8: 568, 9: 418, 10: 512, 11: 568, 12: 418})
while True:
    d.set_speed({i: 100 for i in range(1,7)})
    d.set_goal_position({1: 512, 2: 476, 3: 519})
    time.sleep(0.6)
    d.set_goal_position({4: 512, 5: 547, 6: 504})
    time.sleep(0.4)
    d.set_speed({i:800 for i in range(1,7)})
    d.set_goal_position({1: 512, 2: 694, 3: 401, 4: 512, 5: 329, 6: 622})
    time.sleep(0.6)