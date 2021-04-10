''' Manages the Pi Camera object and image processing operations '''
from time import sleep
import base64
from picamera import PiCamera

def get_image_data(image_name:str, image_extension:str=".jpg")->str:
    '''Gets image data as bytes for ready to post'''
    with open(f'{image_name}{image_extension}','rb') as image_file:
        image_data = image_file.read()
    return base64.b64encode(image_data).decode() # To fit in json.dumps()


def init_cam()-> PiCamera():
    '''Initiates a Pi Camera with correct rotation'''
    camera:PiCamera = PiCamera()
    camera.rotation=270 # To fix image output
    camera.start_preview()
    sleep(2) #Wait until init is done
    return camera
