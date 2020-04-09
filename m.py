import dxl

a = dxl.get_available_ports()
d = dxl.dxl(a[0], 1000000)

print("1:{0}, 2:{1}, 3:{2}, 4:{3}, 5:{4}".format(d.read(1), d.read(2), d.read(3), d.read(4), d.read(5)))
