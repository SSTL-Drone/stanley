#!/bin/bash

pip install dronekit dronekit-sitl pymavlink pytest depthai-sdk

# Might be needed?
bash -c "$(curl -fL https://docs.luxonis.com/install_dependencies.sh)"