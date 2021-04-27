# APP

1) This app should run on server not on raspberry pi.

# Install nodejs to the server

1) curl to node setup.

```curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -```

2) install nodejs

 ```sudo apt install nodejs```

3) check version

```node --version ```

* output:

```v14.2.0```

```npm --version```

* output:

```6.14.4```

4) To be able to compile native addons from npm you’ll need to install the development tools:

```sudo apt install build-essential```

# Install nginx to ubuntu

1) Update Software Repositories

```sudo apt-get update```

2) Install Nginx From Ubuntu Repositories

```sudo apt-get install nginx```

3) Verify the Installation

```nginx -v```

4) Allow Nginx Traffic

    * install firewalld

    ```sudo apt-get install firewalld```

    * Configure firewall rules

    ```sudo firewall-cmd --add-service=http --permanent```

    ```sudo firewall-cmd --add-service=https --permanent```

    ```sudo firewall-cmd --reload```

5) Enable and start the NGINX service

    ```sudo systemctl enable --now nginx.service```

    * The service starts a web server that listens on TCP port 80 by default. To check the status of the service, run this command:

    ```sudo systemctl status nginx```

    * Test your deployment: With your web browser, go to the domain name or IP address of your system.(You will see nginx template html)

        http://myserver.example.com/



# Deploying frontend to ubuntu

1) clone [pi-cctv](https://github.com/novitai/pi-cctv) to the server:

    ```git clone https://github.com/novitai/pi-cctv.git```

2) cd into frontend folder

    ```cd pi-cctv/app/frontend```

3) install npm packages:

    ```npm install```

4) Assumed that you did your tests with: ```npm start``` Build your frontend.

    ```npm run build```

    * build folder will be created copy build folder to /var/www/build folder for nginx configration:

    ```sudo cp -r buildfolder /var/www/buildfolder```

5) Update the NGINX configuration

    * install nano for editing config file:

    ```sudo apt-get install nano```



    * default conf is port 80. first just change root to /var/www/buildfolder in nginx conf and check the ip on your browser, then continue https configrations.

    ```sudo nano /etc/nginx/sites-available/default```

            server {
                        root         /var/www/buildfolder;

                    }

    * reload nginx before testing on your browser:

    ```sudo nginx -s reload```

    * setup your domain to ip address before certificate setup

    * install certbot

        ```sudo apt-get install certbot python3-certbot-nginx```

    * create certificate:

        ```sudo certbot certonly --nginx```

    * configure sertificate in nginx:

        ```sudo certbot install --nginx```

        ```sudo nginx -s reload```

    * test on your browser https.

# Deploying fastapi and frontend into same instance


1) install pip3 , python3

    ```sudo apt-get install python3-pip```

2) cd into fastapi directory

    ```cd pi-cctv/app/api ```

3) install requirements

    ```pip3 install -r requirements.txt```

4) if the frontend build is not setup for fast api look [this solution](https://stackoverflow.com/questions/62928450/how-to-put-backend-and-frontend-together-returning-react-frontend-from-fastapi) then continue fastapi deployement

5) run the server with certificates:

    ```sudo -E python3 -m uvicorn main:app --host 0.0.0.0 --port 443 --ssl-keyfile=/etc/letsencrypt/live/picamera.novit.ai/privkey.pem --ssl-certfile=/etc/letsencrypt/live/picamera.novit.ai/fullchain.pem```
6) test on your browser
