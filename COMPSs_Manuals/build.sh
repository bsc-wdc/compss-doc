#!/usr/bin/env bash

# 1st step: activate the virtual environment
source documentation-builder/bin/activate

make clean
make -b html
# make latexpdf  # Fails with latest versions, waiting to be patched.

# End step: deactivate environment
deactivate