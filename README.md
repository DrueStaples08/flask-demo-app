# This is a simple application template for any user to clone build off of for their own projects.


### How to run app

1. docker build --target fr_dev -t myapp-1:latest .

2. docker run -d -p 5000:5000 myapp-1

### List containers

- docker ps
- docker container ls

### Stop container
- docker stop name_of_container_when_runnning_docker_ps


### Send to DockerHub

1. Tag Image (serialized number below is the image id)

`docker tag 36f74046cfed druestaples/myapp-1:latest`

2. Push Image 

`docker push druestaples/myapp-1:latest`  


<!-- `docker build -t myapp-1:latest .`
  860  docker build --target fr_dev -t myapp-1:latest .
  861  docker ps
  862  docker run -d -p 5000:5000 myapp-1 -->
