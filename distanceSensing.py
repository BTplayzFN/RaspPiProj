from gpiozero import DistanceSensor
from time import sleep

Echo = 27
Trigger = 17
  
sensor = DistanceSensor(echo = Echo, trigger = Trigger)
def objectClose(threshold = 60):
    try:
      while True:
        cmDistance = sensor.distance * 100
        if cmDistance < threshold:
          return True
        else:
          return False
          sleep(0.1)
    # this except gotta be changed to the button or whatever we want it to be
    except KeyboardInterrupt:
      return False
