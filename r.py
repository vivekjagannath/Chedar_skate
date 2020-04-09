import dxl
import time

a = dxl.get_available_ports()
d = dxl.dxl(a[0], 1000000)
d.set_torque({i:1 for i in range(1,6)})
d.set_speed({i:30 for i in range(1,6)})
d.set_goal_position({i:2048 for i in range(1,6)})
time.sleep(4)
d.set_goal_position({1:2104, 2:1723, 3:1113, 4:2637, 5:2141})
time.sleep(4)
d.set_goal_position({1:2101, 2:1396, 3:923, 4:2637, 5:2131})
time.sleep(4)

d.set_goal_position({1:2104, 2:1723, 3:1113, 4:2637, 5:2141})
time.sleep(4)

d.set_goal_position({1:2104, 2:1523, 3:1113, 4:2637, 5:2141})
time.sleep(4)
d.set_speed({3:50})
d.set_goal_position({i:2048 for i in range(1,6)})
