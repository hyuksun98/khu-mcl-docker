## khu-mcl-docker

### app.py
This script runs a simple web server using Flask and 
demonstrates a client sending a message to the server.

The server runs in a new thread, while the client
sends a message to the server after a certain delay
and prints the server's response.

Environment veriables are used to set the server's port and the client's message.

### How to use

1) Clone the repository

2) Move to ```khu-mcl-docker```

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
