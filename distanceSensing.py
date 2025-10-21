from gpiozero import DistanceSensor
from time import sleep

Echo = 27
Trigger = 17
  
sensor = DistanceSensor(echo = Echo, trigger = Trigger)

#this will be imported by the main function or something along those lines to determine whether to run or not
def objectClose(threshold = 60):
    try:
      while True:
        cmDistance = sensor.distance * 100
        if cmDistance < threshold:
          yield True 
        else:
          yield False
        sleep(0.1)
    # this except gotta be changed to the button or whatever we want it to be
    except KeyboardInterrupt:
      return 
