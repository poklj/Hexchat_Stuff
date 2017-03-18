import time

TimeX = 0

def check_timeclash(*args):
    global TimeX
    TimeY = 0
    if args[0] == 1:
        TimeX = 0
        TimeX = TimeX + time.time()
        print(str(TimeX))
    if args[0] == 2:
        TimeY = time.time()
        print(str(TimeY))
        #if ((TimeX + 250) <= TimeY):

        if int(TimeX)+ 10 < int(TimeY):
            print(TimeX+10)
            print("lessthen")
        else:
            print(TimeX+10)
            print("greaterthen0")


print("3 second test \n")
check_timeclash(1)
time.sleep(3)
check_timeclash(2)
print("-----\n")
print("11 second test")
check_timeclash(1)
time.sleep(14)
check_timeclash(2)