#!/bin/bash

docker build -t ksithvothy/haproxy:1.7 .

if [ $? = 0 ]; then
    docker push ksithvothy/haproxy:1.7
fi