import dxl
import time
a = dxl.get_available_ports()
print(a)
d = dxl.dxl(a[0], 1000000, 1, True)
# To scan for available motors:
print(d.scan(11))
# To move a motor:
d.set_torque({i:1 for i in range(1,11)})
stance={}
ini={}
inp=1
d.set_speed({i:30 for i in range(1,11)})
for i in range(1,11):
    d.speed(i,30)
    ini[i]=d.read(i)
    time.sleep(1)

print(ini)
st="no"

while True:
    ids=input("enter motor id:")
    if ids=="exit":
        break
    elif ids=="zero":
        d.set_goal_position({1: 2051, 2: 2041, 3: 2054, 4: 2052, 5: 2050, 6: 2092, 7: 2070, 8: 1903, 9: 1614, 10: 2081})

    elif ids=="init":
        # d.set_goal_position({1:2048,2:2048,3:2048,4:2048,5:2048,6:2048,7:2048,8:2048,10:2048})
        d.set_speed({3:100,4:60,7:100,9:60})
        d.set_goal_position({1: 2079, 2:(4096-2373), 3:(4096-2578), 4:2378, 5: 2088, 6: 2074, 7: 2373, 8: 2578, 9: 1921, 10: 2078})
        time.sleep(2)
        # d.set_torque({4:0,9:0})

        # 4:2048+(1601-1464)
        # 3:(4096-2578)
        # 2:(4096-2373)
        # 1:2048
        
        print("initial")
        time.sleep(2)
    elif ids=="walk":
        d.set_goal_position({1: 2076, 2:1812, 3:1574, 4: 2375, 5: 2084, 6:2073, 7:2413, 8:2672, 9:1995, 10:2099})
        time.sleep(0.8)
        d.set_goal_position({1: 2076, 2: 1727, 3: 1472, 4: 2383, 5: 2083, 6: 2074, 7: 2210, 8: 2542, 9: 1996, 10: 2094})
    elif ids=="nol":
        d.set_torque({i:0 for i in range(6,11)})
        s=input()
        if s=="go":
            d.set_torque({i:1 for i in range(6,11)})
            goalpos={}
            for i in range(1,11):
                d.speed(i,30)
                goalpos[i]=d.read(i)
                time.sleep(0.5)
            print(goalpos)
            temp=input("Enter name of stance")
            f=open(temp+".txt",'a+')
            f.write(str(goalpos))
            f.close()
    elif ids=="nor":
        d.set_torque({i:0 for i in range(1,6)})
        s=input()
        if s=="go":
            d.set_torque({i:1 for i in range(1,6)})
            goalpos={}
            for i in range(1,11):
                d.speed(i,30)
                goalpos[i]=d.read(i)
                time.sleep(0.5)
            print(goalpos)
            temp=input("Enter name of stance")
            f=open(temp+".txt",'a+')
            f.write(str(goalpos))
            f.close()


    elif ids=="liftr":
        d.set_goal_position({1: 2048, 2: 1880, 3: 1884, 4: 2062, 5: 2101, 6: 2053, 7: 2305, 8: 3005, 9: 1858, 10: 2164})
        time.sleep(5)
        d.set_goal_position({1: 2053, 2: 1872, 3: 1874, 4: 2058, 5: 2103, 6: 2051, 7: 2306, 8: 2827, 9: 2099, 10: 2098})
        time.sleep(5)
        d.set_goal_position({1: 2057, 2: 1864, 3: 1868, 4: 2056, 5: 2108, 6: 2119, 7: 2312, 8: 2316, 9: 1785, 10: 2062})
    elif ids=="bend":
        for i in range(2):
            d.speed(3,60)
            d.set_goal_position({1: 2048, 2: 1680, 3: 1113, 4: 2048+229, 5: 2048})
            time.sleep(5)
            d.speed(3,30)
            d.set_goal_position({1: 2048, 2: 1345, 3: 884, 4: 2048+229, 5: 2100})
            time.sleep(5)
        d.set_goal_position({1: 2048, 2: 1580, 3: 1113, 4: 2048+229, 5: 2048})
        time.sleep(3)
        d.speed(3,60)
        d.set_goal_position({2:2048,3:2048,4:2048})
        print("Done")
    elif ids=="read":
        d.set_torque({i:0 for i in range(1,11)})
        s=input()
        if s=="go":
            d.set_torque({i:1 for i in range(1,11)})
            goalpos={}
            for i in range(1,11):
                d.speed(i,30)
                goalpos[i]=d.read(i)
                time.sleep(0.5)
            print(goalpos)
            temp=input("Enter name of stance")
            f=open(temp+".txt",'a+')
            f.write(str(goalpos))
            f.close()
            # stance[temp]=goalpos
        print("done")
    elif ids=="up":
        d.set_goal_position({3:700,4:2048})
        print("step1")
        time.sleep(5)
        d.set_goal_position({1:2048,2:1926,3:1764})
        print("next")
        time.sleep(5)
        print("done")
    # elif ids=="take":
    #     temp=input("Enter stance name")
    #     d.set_torque({i:1 for i in range(1,11)})
    #     d.set_goal_position(stance[temp])
    #     time.sleep(4)
    #     print("done")        
    else:
        while True:
            inp=int(input("enter 0 to exit else enter goal:"))
            if inp==0:
                st=input("Enter description:")
                f=open("vals.txt",'a+')
                f.write("motor id = "+str(ids)+" "+st+" angle="+str(ini[int(ids)])+"\n")
                f.close()
                break
            else:
                ini[int(ids)]=ini[int(ids)]+inp
                d.move(int(ids), ini[int(ids)])
                print(ini[int(ids)])
#To read angle:
#d.read(id)
#To change id:
#d.change_id(old_id, new_id)
