#!/bin/bash

docker build -t oudamdevops/haproxy:1.7-alpine .

if [ $? = 0 ]; then
    docker push oudamdevops/haproxy:1.7-alpine
fi