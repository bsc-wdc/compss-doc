#!/usr/bin/env bash

# 1st step: activate the virtual environment
if [ ! -f "documentation-builder/bin/activate" ]; then
    echo "Virtual environment not found. Creating..."
    ./create_venv.sh
    echo "Virtual environment created: OK"
fi
source documentation-builder/bin/activate

make clean

# End step: deactivate environment
deactivate

rm -rf documentation-builder
rm -rf build
