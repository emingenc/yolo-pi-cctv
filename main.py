''' Manages the main loop of the pi-camera system '''
from time import sleep
import argparse
import socket
import json
import requests
import os
from camera import init_cam, get_image_data

def detect_obj(source:str='./img.jpg' ,project_name:str='new_detect'):
    os.system(f'python3 ../yolov5/detect.py --source {source} --save-txt --project {project_name} --exist-ok')  

def post_image(frame:int, image_name:str, image:str, url:str)-> requests.Response:
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
    camera = init_cam()
    frame_count=0
    for filename in camera.capture_continuous(f'{file_name}.jpg'):
        detect_obj(source=f'{file_name}.jpg')
        sleep(5) 
        frame_count += 1
        base64_image = get_image_data(f'new_detect/exp/{file_name}')
        try:
            post_image(
                        frame=frame_count,
                        image_name=filename,
                        image=base64_image,
                        url='http://192.168.1.25:8000/images/')
        except socket.error as error: # To prevent crashes when connection is lost/when pi can not connect
            print('Server connection error ')


if __name__ == "__main__":
    # python3 camera.py --name <filename>
    parser = argparse.ArgumentParser()
    parser.add_argument('--name',default="img", type=str,  help='image file name')
    opt = parser.parse_args()
    run_camera(opt.name)
