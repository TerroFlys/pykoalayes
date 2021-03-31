import pyautogui as pg
from time import sleep
from time import time
#website url: http://www.koalastothemax.com/
#tested on 2k monitor so prob wont work on FHD oopsy
print("starting ")
#Corner Values
#Left top: x= 1030, y=460
#Left down: x= 1030, y=1015
#Right top: x= 1570, y=460
#Right down: x= 1570, y=1015
left_top = [1030, 460] # X, Y
left_down = [1030, 1015]
right_top = [1570, 460]
right_down = [1570, 1015]
print("starting in 4 seconds")
sleep(4)
start_time = time()
print("range: "+ str(left_down[1]) + " - " + str(left_top[1]) + " = " + str(left_down[1] - left_top[1]))
print("\nEstimated time: " + str((left_down[1] - left_top[1]) * 0.2) + "seconds\n\n")
for i in range(left_down[1] - left_top[1]):
    print(str(i) + " | x1: " + str(left_top[0]) + " , y1: " + str(left_top[1]+i) + " | x2: " + str(right_top[0]) + " ,y2: " + str(right_top[1]+i))
    pg.moveTo(left_top[0],left_top[1]+i,0.05)
    pg.moveTo(right_top[0],right_top[1]+i,0.05)
print("Done in " + str(time() - start_time) + "seconds")
