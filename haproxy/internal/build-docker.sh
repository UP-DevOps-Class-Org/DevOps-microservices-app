#!/bin/bash

docker build -t sithvothykiv/haproxy:1.7-alpine .

if [ $? = 0 ]; then
    docker push sithvothykiv/haproxy:1.7-alpine
fi