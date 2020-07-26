# Docker-Compose Microservices Example

This is a project only focused on my personal studies about docker and docker compose.
I created two microservices, one providing dummy-data and the another one consuming the api 

## How to run 

check if you are in the app directory

```
    npm --prefix ./services/api install ./services/api
    docker-compose -f ./docker/docker-compose.yaml up
```

then when the containers start running you can access http://localhost:5000 to check the output from the service