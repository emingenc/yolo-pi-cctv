from time import sleep
from picamera import PiCamera
import argparse

def run_camera(filename:str)-> None:
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    for filename in camera.capture_continuous(f'{filename}.jpg'):
        print('Captured %s' % filename)
        sleep(2) # wait 2 sec


if __name__ == "__main__":
    # python3 camera.py --name <filename>  
    parser = argparse.ArgumentParser()
    parser.add_argument('--name',default="img", type=str,  help='image file name')
    opt = parser.parse_args()
    run_camera(opt.name)
