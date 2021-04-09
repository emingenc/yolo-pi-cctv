import argparse
import json
import requests
import socket
import base64
from time import sleep
from picamera import PiCamera
from PIL import Image
from io import BytesIO


def get_image_data(image_name:str)->str:
    '''Gets image data as bytes for ready to post'''
    with open(f'{image_name}.png','rb') as image_file:
        image_data = image_file.read()
    return base64.b64encode(image_data).decode() # for to fit in json.dumps()


def compress_image(image_name:str)->None:
    '''Takes image name as an input find it and compress it'''
    with open(f'{image_name}.jpg', "rb") as image_file:
        data = base64.b64encode(image_file.read())
    img = Image.open(BytesIO(base64.b64decode(data)))
    img.save(f'{image_name}.png', 'PNG')


def post_image(frame:int,image_name:str,  image:str, url:str)-> requests.Response:
    '''Sends image and device data to server'''
    device_name = socket.gethostname()
    data_dict: dict = {
                "frame":frame,
                "device_name": device_name,
                "image_name": image_name,
                "image": image              
                                            }
    data:str = json.dumps(data_dict)
    response = requests.post(url,  data=data)
    return response


def run_camera(file_name:str)-> None:
    camera:PiCamera = PiCamera()
    camera.rotation=270 #For to fix image output
    camera.start_preview()
    sleep(2)
    frame_count=0
    for filename in camera.capture_continuous(f'{file_name}.jpg'):
        frame_count += 1
        compress_image(file_name) # compressing image file
        compressed_image = get_image_data(file_name)
        try:
            post_image(
                        frame=frame_count,
                        image_name=filename,
                        image=compressed_image,
                        url='http://192.168.88.132:8000/images/')
        except socket.error as error: # For to prevent crush when connection lost or when pi can not connect
            print('Server connection error ')
        sleep(2) # wait 2 sec


if __name__ == "__main__":
    # python3 camera.py --name <filename>  
    parser = argparse.ArgumentParser()
    parser.add_argument('--name',default="img", type=str,  help='image file name')
    opt = parser.parse_args()
    run_camera(opt.name)
