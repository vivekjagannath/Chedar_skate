import dxl
import time

a = dxl.get_available_ports()
d = dxl.dxl(a[0], 1000000)
d.set_speed({i:100 for i in range(1,13)})
while True:
    d.set_goal_position({1:523, 2:552, 3:559, 4:505, 5:555, 6:370, 7:505, 8:468, 9:653, 10:500, 11:552, 12:559})
    time.sleep(0.6)
    d.set_goal_position({1:518, 2:462, 3:566, 4:582, 5:508, 6:379, 7:582, 8:515, 9:644, 10:505, 11:462, 12:566})
    time.sleep(0.6)
    d.set_goal_position({1:522, 2:462, 3:564, 4:515, 5:512, 6:389, 7:515, 8:512, 9:634, 10:501, 11:462, 12:564})
    time.sleep(0.6)
    d.set_goal_position({1:585, 2:517, 3:612, 4:501, 5:554, 6:363, 7:501, 8:469, 9:660, 10:438, 11:517, 12:612})
    time.sleep(0.6)