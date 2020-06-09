#!/bin/bash

docker image build . -t spori:latest
docker container run -ti --privileged --mount type=bind,source="$(pwd)"/share,target=/root/.spotify-ripper/share spori:latest
