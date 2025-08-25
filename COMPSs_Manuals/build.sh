#!/usr/bin/env bash


# 1st step: activate the virtual environment
if [ ! -f "documentation-builder/bin/activate" ]; then
    echo "Virtual environment not found. Creating..."
    ./create_venv.sh
    echo "Virtual environment created: OK"
fi
source documentation-builder/bin/activate

# Check if dependencies are installed
python3 -c "import enchant; print(enchant.list_languages())" | grep "en"
spelling_dict=$?
if [ $spelling_dict -ne 0 ]; then
    echo "Could not find myspell-en dictionary."
    echo "Please, install package myspell-en"
    deactivate
fi

#make clean
make -b html spelling
# make latexpdf  # Fails with latest versions, waiting to be patched.

# End step: deactivate environment
deactivate


# the convention
#
# ####################################
# Part -- Number Signs above and below
# ####################################
#
# with overline, for parts
#
# ************************************
# Chapter -- Asterisks above and below
# ************************************
#
# with overline, for chapters
#
# Title -- Number Signs
# #####################
#
# Suptitle -- Asterisks
# *********************
#
# Section -- Equal Signs
# ======================
#
# Subsection -- Hyphens
# ---------------------
#
# Subsubsection -- Circumflex
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Paragraph -- Double Quotes
# """"""""""""""""""""""""""
