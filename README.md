# dockerQA


- php 7.1
- php 7.2
- php 7.3
- php 7.4
- mysql 5.7
- mariadb 10.1
- phpmyadmin

## How to install
If the stack is not yet installed on your device
```
git clone https://github.com/SD1982/dockerQA.git
cd dockerQA
bash build.sh
```

## How to start
If the stack is already install to your device
``` 
cd dockerQA
docker-compose up -d
```

## How to use
Add your php app folder (like prestashop for example) in the html folder
go to your localhost with the required port for the required php version
### php versions
- php 7.1 is at localhost:8071/your-app-folder-name
- php 7.2 is at localhost:8072/your-app-folder-name
- php 7.3 is at localhost:8073/your-app-folder-name
- php 7.4 is at localhost:8074/your-app-folder-name
### databases
#### from outside container
- mysql 5.7 is at localhost:3306 (user = root, password = root)
- mariadb is at localhost:3307 (user = root, password = root)
#### from outside container
- mysql 5.7 is at localhost:3306 or with container name qa-mysql-5.7
  (user = root, password = root)
- mariadb is at localhost:3307 or with container name qa-mariadb-5.7
  (user = root, password = root)
###phpmyadmin
- phpmyadmin is accessible at localhost:8100 and can connect to both databases 
  (server = (qa-mysql-5.7 or qa-mariadb-10.1) user = root, password = root)
