from io import BytesIO
from time import sleep
import socket
import base64
import argparse
import json
import requests
from picamera import PiCamera


def get_image_data(image_name:str, image_extension:str=".jpg")->str:
    '''Gets image data as bytes for ready to post'''
    with open(f'{image_name}{image_extension}','rb') as image_file:
        image_data = image_file.read()
    return base64.b64encode(image_data).decode() # To fit in json.dumps()


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
    camera.rotation=270 # To fix image output
    camera.start_preview()
    sleep(2)
    frame_count=0
    for filename in camera.capture_continuous(f'{file_name}.jpg'):
        frame_count += 1
        base64_image = get_image_data(file_name)
        try:
            post_image(
                        frame=frame_count,
                        image_name=filename,
                        image=base64_image,
                        url='http://192.168.88.132:8000/images/')
        except socket.error as error: # To prevent crashes when connection is lost/when pi can not connect
            print('Server connection error ')
        sleep(2) # wait 2 sec


if __name__ == "__main__":
    # python3 camera.py --name <filename>
    parser = argparse.ArgumentParser()
    parser.add_argument('--name',default="img", type=str,  help='image file name')
    opt = parser.parse_args()
    run_camera(opt.name)
