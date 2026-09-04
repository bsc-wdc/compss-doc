#!/usr/bin/env bash


# 1st step: activate the conda environment (create it first)
source activate_conda.sh

# Check if dependencies are installed
python3 -c "import enchant; print(enchant.list_languages())" | grep "en"
spelling_dict=$?
if [ $spelling_dict -ne 0 ]; then
    echo "Could not find myspell-en dictionary."
    echo "Please, install package myspell-en"
    conda deactivate
fi

#make clean
make -b html spelling
# make latexpdf  # Fails with latest versions, waiting to be patched.

# End step: deactivate environment
conda deactivate
