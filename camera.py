from time import sleep
from picamera import PiCamera

if __name__ == "__main__":
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    for filename in camera.capture_continuous('img.jpg'):
        print('Captured %s' % filename)
        sleep(2) # wait 2 sec
        