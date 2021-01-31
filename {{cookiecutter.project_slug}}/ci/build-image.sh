#!/bin/bash -e

docker build --force-rm -t $3 -f $1 $2 --build-arg PIP_PACKAGES=.tmp/pip-packages
