#!/bin/bash


pip install lxml==4.8.0
pip install git+https://github.com/dronekit/dronekit-python.git
pip install dronekit-sitl pymavlink pytest depthai-sdk gpxpy websockets asyncio

# Might be needed?
bash -c "$(curl -fL https://docs.luxonis.com/install_dependencies.sh)"