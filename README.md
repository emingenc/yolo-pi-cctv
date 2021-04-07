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

        ```git clone https://github.com/novitai/pi-cctv.git```

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
