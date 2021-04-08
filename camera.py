from time import sleep
from picamera import PiCamera
import argparse
import requests
import socket


def post_image(image_name:str,  image:str, url:str)-> None:
    device_name = socket.gethostname()

    data = f'"device_name": "{device_name}", "image_name": "{image_name}", "image": "{image}"'
    data = '{'+data+'}'

    response = requests.post(url,  data=data)
    return response

def run_camera(filename:str)-> None:
    camera = PiCamera()
    camera.rotation=270
    camera.start_preview()
    sleep(2)
    count = 0
    for filename in camera.capture_continuous(f'{filename}.jpg'):
        count += 1 
        try:
            post_image(image_name=filename,image=count,url='http://192.168.88.132:8000/images/')
        except socket.error as error:
            print('Server connection error ')
        sleep(2) # wait 2 sec


if __name__ == "__main__":
    # python3 camera.py --name <filename>  
    parser = argparse.ArgumentParser()
    parser.add_argument('--name',default="img", type=str,  help='image file name')
    opt = parser.parse_args()
    run_camera(opt.name)