from time import sleep
from picamera import PiCamera
import argparse
import requests
import socket


def post_image(image_name:str,  image:list, url:str)-> None:
    device_name = socket.gethostname()
    data = {
                'device_name': device_name,
                'image_name': image_name,
                'image': image,     
                                            }

    post_data = requests.post(url = url, data = data)


def run_camera(filename:str)-> None:
    camera = PiCamera()
    camera.rotation=270
    camera.start_preview()
    sleep(2)
    for filename in camera.capture_continuous(f'{filename}.jpg'):
        #post_image(image=img,url='http://192.168.88.132:8000/images')
        sleep(2) # wait 2 sec


if __name__ == "__main__":
    # python3 camera.py --name <filename>  
    parser = argparse.ArgumentParser()
    parser.add_argument('--name',default="img", type=str,  help='image file name')
    opt = parser.parse_args()
    run_camera(opt.name)
