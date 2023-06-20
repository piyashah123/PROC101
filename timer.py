# implementing timer 
# import a time module
import time

# input time in seconds
seconds=input("enter the time in seconds:");

# define a coutdown time function
def coutdown_timer(seconds):
    while seconds > 0 :
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        seconds-=1
        print(timer,end='\r')
        time.sleep(1)
 

# calling the function
coutdown_timer(int(seconds)) 