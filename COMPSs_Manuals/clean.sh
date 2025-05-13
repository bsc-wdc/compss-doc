#!/usr/bin/env bash

# Clean the virtual environment
if [ -f "documentation-builder/bin/activate" ]; then
  source documentation-builder/bin/activate
  make clean
  deactivate
fi

rm -rf documentation-builder
rm -rf build
