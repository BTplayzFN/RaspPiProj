from gpio import MotionSensor
from time import sleep, time
from distanceSensing import objectClose

PIR_PIN = 22 #change for whatever 
motion = MotionSensor(PIR_Pin)

def detectCloseMotion(timeout=10)
  for isClose in objectClose(threshold):
    if isClose:
      while True:
        try:
          #double check to see if still close enough to run
          if not next(objectClose(threshold)):
            return
            #yields true or false if motion detected nearby
          if motion.motion_detected:
            yield True
          else:
            yield False
          sleep(0.1)
        except StopIteration:
          return
    else:
      #just stays waiting for it to be close
      sleep(0.1)
