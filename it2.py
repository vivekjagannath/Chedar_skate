import dxl
import time
d.set_speed({i:200 for i in range(1,13)})
d.set_goal_position({i:512 for i in range(1,13)})
time.sleep(2)
d.set_goal_position({1: 523, 2: 581, 3: 525, 4: 456, 5: 537, 6: 425})
time.sleep(0.3)
d.set_goal_position({1: 510, 2: 464, 3: 561, 4: 579, 5: 469, 6: 446})
time.sleep(0.3)
d.set_goal_position({1: 510, 2: 464, 3: 561, 4: 579, 5: 469, 6: 446})
time.sleep(0.3)
d.set_goal_position({1: 594, 2: 537, 3: 564, 4: 486, 5: 554, 6: 435})
time.sleep(0.2)
d.set_goal_position({i:512 for i in range(1,13)})