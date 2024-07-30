## khu-mcl-docker

### 0. FYI
Because this repository was designed for a lab seminar,
code efficiency aspects were not considered.

So, please keep in mind that this is simply a repository
for learning 'Docker'.

### 1. app.py
This script runs a simple web server using 'Flask' and 
demonstrates a client sending a message to the server.

The server runs in a new thread, while the client
sends a message to the server after a certain delay
and prints the server's response.

### 2.Dockerfile
Environment variables are used to set the server's port and the client's message
at the time running 'Docker Container'.

USER_NAME variable will be set while building docker-image.

### 3. How to use

1) Clone the repository


2) Move to ```khu-mcl-docker```
```shell
cd khu-mcl-docker
```


3) Build Docker Image
```shell
docker build --build-arg USER_NAME=$USER -t flask_app:latest .
```


4) Run the Container
```shell
docker run -p 3000:5000 -e FLASK_PORT=5000 -e CLIENT_MESSAGE="Hello from $USER!" --name flask_server flask_app:latest
```


5) Enter into the Container
```shell
docker exec -it flask_server /bin/bash

# Exit Container
exit
```
