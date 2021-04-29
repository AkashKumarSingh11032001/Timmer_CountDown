import time

def countDown(t):
    while(t):
        min, sec = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(min,sec)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    
    print("CountDown Over")

t = input("Enter time in second: ")
countDown(int(t))