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



# Deploying frontend to 

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

    ```sudo nano /etc/nginx/sites-available/default```

    * default conf is port 80. first just change root to /var/www/buildfolder in nginx conf and check the ip on your browser, then continue https configrations.

            server {
                        listen       443 ssl http2 default_server;
                        listen       [::]:443 ssl http2 default_server;
                        server_name  _;
                        root         /var/www/buildfolder;

                        ssl_certificate "/etc/pki/nginx/server.crt";
                        ssl_certificate_key "/etc/pki/nginx/private/server.key";
                        ssl_session_cache shared:SSL:1m;
                        ssl_session_timeout  10m;
                        ssl_ciphers PROFILE=SYSTEM;
                        ssl_prefer_server_ciphers on;

                        # Load configuration files for the default server block.
                        include /etc/nginx/default.d/*.conf;

                        location / {
                        }

                        error_page 404 /404.html;
                            location = /40x.html {
                        }

                        error_page 500 502 503 504 /50x.html;
                            location = /50x.html {
                        }
                    }