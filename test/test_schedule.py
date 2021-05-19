import time
import datetime

def job():
    print("I'm working...",datetime.datetime.now())

first_time = True
check_15m = False
check_1h = False
check_4h = False
while True:
    now = datetime.datetime.now()
    h = now.hour
    m = now.minute
    time.sleep(1)
    
    if first_time:
        check_15m = True
        check_1h = True
        check_4h = True
        first_time = False
        print("first time",now)
    
    if m % 15 == 0:
        if not check_15m:
            # something to do
            print("15")
            check_15m = True
    else:
        check_15m = False
    

    if m == 0:
        if not check_1h:
            # something to do
            print("1h")
            check_1h = True
    else:
        check_1h = False


    if h % 4 == 0:
        if not check_4h:
            # something to do
            print("4h")
            check_4h = True
    else:
        check_4h = False