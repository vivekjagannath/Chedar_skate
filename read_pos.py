import dxl
a = dxl.get_available_ports()
d = dxl.dxl(a[0], 1000000)

d.set_torque({i : 0 for i in range(1,13)})
input()
print("1: {0}, 2: {1}, 3: {2}, 4: {3}, 5: {4}, 6: {5}, 7: {6}, 8: {7}, 9: {8}, 10: {9}, 11: {10}, 12: {11}".format(d.read(1), d.read(2), d.read(3), d.read(4), d.read(5), d.read(6), d.read(7), d.read(8), d.read(9), d.read(10), d.read(11), d.read(12)))
