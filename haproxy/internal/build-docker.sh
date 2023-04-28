#!/bin/bash

docker build -t sithvothykiv/haproxy:1.7 .

# if [ $? = 0 ]; then
#     docker push sithvothykiv/haproxy:1.7
# fi