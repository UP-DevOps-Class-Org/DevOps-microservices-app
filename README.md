# Deploy Microservices using Docker-swarm and HAProxy

## Step 1 : 
### *NOTE: Make sure that you have installed docker in each nodes*

**ssh into Node**

```
kivsithvothy@Kivs-MBP ~ % ssh root@your-public-ip
```

## Step 2 : 

- **Create a new docker-swarm**

```
root@swarm-node~# docker swarm init

Swarm initialized: current node (b4etd4utcgn9xnpawfs2tf5qe) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-0hbyhpos06fwf85r35319wyhjpfysk9l88emio2av1qsr04alu-8th0xvea2f0yw3voiqc5er32c 192.168.99.100:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

```
- **Go to the other worker nodes and join the worker nodes to swaram manager**

```
root@swarm-node~# docker swarm join --token SWMTKN-1-0hbyhpos06fwf85r35319wyhjpfysk9l88emio2av1qsr04alu-8th0xvea2f0yw3voiqc5er32c 192.168.99.100:2377

root@swarm-node~# docker ndoe ls
```
## Step 3 : 
### Run a command 

- Clone the repository
``` 
root@swarm-node~# git clone https://github.com/UP-DevOps-Class-Org/DevOps-microservices-app.git

root@swarm-node~# cd DevOps-microservices-app

```
- Deploy all microservices
``` 
root@swarm-node~# python3 deploy.py all
```
- Deploy one microservice

```
root@swarm-node~# python3 deploy.py app1_name

```
- Deploy multi microservices

```
root@swarm-node~# python3 deploy.py app1_name app2_name app3_name
```

**Run docker container**
```
docker run -d -p 7500:7500 image-id
```