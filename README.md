### Basic FastAPI CRUD API

A Basic FastAPI based CRUD backend API without any database connection.

### How to use?

- Clone the Repo using: `git clone https://github.com/theinfosecguy/fastapi`
- Change Directory: `cd fastapi`
- Start Docker on your machine
- Use command: `sudo docker-compose up`

### How to Deploy on EC2 using NGINX?

- go to folder `cd /etc/nginx/sites-enabled`
- create new file (exmample `sudo torch test_ssl`)
    ``` text
    server  {
        listen 80;
        server_name {your ip aws}; (example : 00.000.00.000)
        location / {
            proxy_pass http://127.0.0.1:8000;
        }
    }
    ```


### How to have DNS?

 - go to [epik](https://registrar.epik.com/domain/portfolio)
 - buy your DNS
 - DNS Record

### How to setting https?
 - go to link `https://manage.sslforfree.com/certificates`
 - Document how to install on nginx is [Here](https://help.zerossl.com/hc/en-us/articles/360058295894-Installing-SSL-Certificate-on-NGINX)
 - `cat certificate.crt ca_bundle.crt >> certificate.crt`
 - install file on your project (exammple : `dewasmith.xyz`)
 ``` bash
    server {

        listen               443 ssl;

        ssl                  on;
        ssl_certificate      /home/ubuntu/fastapi/dewasmith.xyz/certificate.crt;
        ssl_certificate_key  /home/ubuntu/fastapi/dewasmith.xyz/private.key;


        server_name  dewasmith.xyz;
        access_log   /var/log/nginx/nginx.vhost.access.log;
        error_log    /var/log/nginx/nginx.vhost.error.log;

        location / {
                proxy_pass http://127.0.0.1:8000;
        }
    }

 ```

 ----
 ### How to have Sql server?
- bring this to docker-compose.yml
``` text
    sql-server-db:
    container_name: sql-server-db
    image: microsoft/mssql-server-linux:2017-latest
    ports:
      - "1433:1433"
    environment:
      SA_PASSWORD: "strong_password"
      ACCEPT_EULA: "Y"
```