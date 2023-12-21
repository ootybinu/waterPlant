import time
import os
#from machine import Pin
schHour=19
schMin=30
scheduleTime=60
def monitor():
    currenttime =time.localtime()
    hour = currenttime.tm_hour
    minute = currenttime.tm_min
    print ("Monitoring at ", currenttime)

    if (hour<schHour-1):
        #early morning
        if (os.path.exists('completed')):
            os.remove('completed')
            print("Removed completed")
        #scheduleTime=60*60
        pause(60*60)
    elif (hour == schHour -1):
        #scheduleTime=60
        pause(60)
    elif (hour == schHour and minute < schMin):
        #scheduleTime=60
        pause(60)
    elif(hour >= schHour and minute >= schMin):
        if (os.path.exists('completed')):
            #scheduleTime=60*60
            pause( 60 * 60)
        else:
            execute()
    elif (hour>= schHour and minute < schMin):
        if (os.path.exists('completed')):
            #scheduleTime=60*60
            pause( 60 * 60)
        else:
            execute()




def execute():
    print ("Staring task execution")
    #pin_motor =Pin(12,mode=Pin.Out)
    #pin_motor.on()
    time.sleep(70)
    #pin_motor.off()
    with open('completed',"w") as file:
        print ("Task Completed")
        monitor()

def pause(delaySeconds):
    print("Going to sleep for ", delaySeconds)
    time.sleep(delaySeconds)
    monitor()

monitor()
