#!/usr/bin/env bash

# This script is aimed at creating a conda environment for building the documentation in local machines,
# with the objective of not messing around with the system or user packages.
# For Read the docs it will use directly the requirements.txt file.

unset PYTHONPATH 
unset PYTHONHOME

# 1st step: create conda environment
conda env create -f doc/requirements.yaml

