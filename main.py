''' Manages the main loop of the pi-camera system '''
from time import sleep
import argparse
import socket
import json
import requests
import os
from camera import init_cam, get_image_data
from detect import detect 

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


def main(file_name:str,obj:str='person')-> None:
    camera = init_cam()
    frame_count=0
    for filename in camera.capture_continuous(f'data/images/{file_name}.jpg'):
        detected_objects = detect(
                                    source=f'data/images/{file_name}.jpg',
                                    weights='pawn.pt',
                                    imgsz = 280,
                                    conf_thres = 0.4,
                                    iou_thres = 0.5,
                                    classes=range(300))
        sleep(3)
        frame_count += 1
        base64_image = get_image_data(f'data/output/{file_name}')
        try:
            if obj in detected_objects:
                post_image(
                            frame=frame_count,
                            image_name=filename,
                            image=base64_image,
                            url='http://192.168.1.25:8000/images/')
            else:
                print(f'{obj} not detected')
                sleep(3) # wait for not to overload on pi
        except socket.error as error: # To prevent crashes when connection is lost/when pi can not connect
            print('Server connection error ')
            sleep(3) # wait for not to overload on pi


if __name__ == "__main__":
    # python3 camera.py --name <filename>
    parser = argparse.ArgumentParser()
    parser.add_argument('--file-name',default="img", type=str,  help='image file name')
    parser.add_argument('--obj',default="bottle", type=str,  help='detection class name')
    opt = parser.parse_args()
    args = vars(opt)
    print(args)

    main(**args)
