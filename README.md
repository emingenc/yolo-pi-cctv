# pi-cctv

1) Setup your raspberry pi with [Raspberry Pi instructions](https://github.com/novitai/setuptools/tree/master/raspberrypi) 
2) Enable your camera 
    
    * Make sure your camera connected to your Raspberry Pi :
        
        ```sudo raspi-config```

        select interface options and enable your camera. It will ask you to reboot if not reboot device with: 
        
        ```sudo reboot```
3) Clone this repo :

    * Before clone install git:

        ```sudo apt update```

        ```sudo apt install git```

        ```git clone https://github.com/emingenc/pi-cctv.git```

        ```cd pi-cctv```

4) Install requirements:

    * before installinng requirements.txt create venv:

        4a. Install python3-venv: 
        
        ```sudo apt-get install python3-venv```

        4b. Create venv:

        ```python3 -m venv venv```

        4c. Activate venv:

        ```source venv/bin/activate```

        4d. Install requirements.txt:

        ```pip3 install -r requirements.txt```

5) Auto-start at boot:

    * open etc/profile:

    ```sudo nano /etc/profile```

    * add these commands end of the file
        
    ```source /home/pi/pi-cctv/venv/bin/activate```

    ```cd /home/pi/pi-cctv```

    ```python3 /home/pi/pi-cctv/main.py &```
        
        a. ctrl+x 
        b. save(press y)
        c. press Enter to save file 

6) apt-get requirements for image compression:

    * install:

        ```sudo apt-get install libopenjp2-7 libtiff5```


7)  Torch and torchvision install to pi:

    * you can clone this repo and install via wheel:


        ```git clone https://github.com/Kashu7100/pytorch-armv7l ```

        ```cd pytorch-armv7l```

        ```pip3 install torch-1.7.0a0-cp37-cp37m-linux_armv7l.whl```

        ```pip3 install torchvision-0.8.0a0+45f960c-cp37-cp37m-linux_armv7l.whll```

        note detect.py will not run unless you dont comment out torch and torchvision from requiremnts.txt.


# Custom object detection

1) Train a model with dataset [Check this tutorial](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data) 

2) After you trained a model copy model weights which extension is .pt to this repo.

3) Change weight parameter with weight you just copied in main.py detected_objects detect function

4) run your main.py with object class name that you want to send post request to the server.

    ```python3 camera.py --file-name <filename> --obj <obj_name>```
