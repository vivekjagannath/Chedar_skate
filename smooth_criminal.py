import dxl
import time
a = dxl.get_available_ports()
d = dxl.dxl(a[0], 1000000)
d.set_speed({i: 200 for i in range(1,13)})
d.set_goal_position({i: 512 for i in range(1,13)})
time.sleep(2)
while True: 
    d.set_goal_position({1: 512, 2: 462, 3: 390, 4: 510, 5: 391, 6: 609, 7: 537, 8: 469, 9: 384, 10: 534, 11: 618, 12: 369})
    time.sleep(0.6)
    d.set_goal_position({1: 521, 2: 652, 3: 332, 4: 500, 5: 555, 6: 629, 7: 522, 8: 630, 9: 330, 10: 520, 11: 481, 12: 393})
    time.sleep(0.6)
# d.set_torque({i : 0 for i in range(1,13)})
# input()
# print("1: {0}, 2: {1}, 3: {2}, 4: {3}, 5: {4}, 6: {5}, 7: {6}, 8: {7}, 9: {8}, 10: {9}, 11: {10}, 12: {11}".format(d.read(1), d.read(2), d.read(3), d.read(4), d.read(5), d.read(6), d.read(7), d.read(8), d.read(9), d.read(10), d.read(11), d.read(12)))
