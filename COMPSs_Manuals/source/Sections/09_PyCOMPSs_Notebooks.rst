==================
PyCOMPSs Notebooks
==================

This section contains all PyCOMPSs related tutorial notebooks.

It is divided into three main folders:

1. **Syntax**: Contains the main tutorial notebooks. They cover the syntax and main functionalities of PyCOMPSs.
2. **Hands-On**: Contains example applications and hands-on exercises.
3. **Demos**: Contains demonstration notebooks.

.. toctree::
    :maxdepth: 2
    :caption: Table of Contents

    09_PyCOMPSs_Notebooks/01_Syntax
    09_PyCOMPSs_Notebooks/02_Hands-on
    09_PyCOMPSs_Notebooks/03_Demos


.. HINT::

    These notebooks can be used within **MyBinder**, with the **PyCOMPSs Player**,
    within **Docker**, within **Virtual Machine** (recommended for Windows) provided by BSC, or locally.

    Prerequisites
        * Using *MyBinder*:

            * Open |Binder|

            .. CAUTION::

                Sometimes it may take a while to deploy the COMPSs infrastructure.

        * Using **PyCOMPSs Player**:

            * ``pycompss-player`` (see :ref:`Sections/08_PyCOMPSs_Player/01_Installation:PyCOMPSs Player Installation`)

        * Using **Docker**:

            * Docker
            * Git

        * Using **Virtual Machine**:

            * VirtualBox

        * For **local** execution:

            * Python 2 or 3
            * Install COMPSs requirements described in :ref:`Sections/01_Installation/01_Dependencies:Dependencies`.
            * Install COMPSs (See :ref:`Sections/01_Installation/02_Building_from_sources:Building from sources`)
            * Jupyter (with the desired ipykernel)
            * ipywidgets (only for some hands-on notebooks)
            * numpy (only for some notebooks)
            * dislib (only for some notebooks)
            * numba (only for some notebooks)
            * Git

    Instructions
        * Using **MyBinder**:

            Just explore the folders and run the examples (they have the same structure as this documentation).

        * Using ``pycompss-player``:

            Check the ``pycompss-player`` usage instructions (see :ref:`Sections/08_PyCOMPSs_Player/02_Usage:Usage`)

            Get the notebooks:

            .. code-block:: bash

                $ git clone https://github.com/bsc-wdc/notebooks.git


        * Using **Docker**:

            Run in your machine:

            .. code-block:: bash

                $ git clone https://github.com/bsc-wdc/notebooks.git
                $ docker pull compss/compss:2.6
                $ # Update the path to the notebooks path in the next command before running it
                $ docker run --name mycompss -p 8888:8888 -p 8080:8080 -v /PATH/TO/notebooks:/home/notebooks -itd compss/compss:2.6
                $ docker exec -it mycompss /bin/bash

            Now that docker is running and you are connected:

            .. code-block:: bash

                $ cd /home/notebooks
                $ /etc/init.d/compss-monitor start
                $ jupyter-notebook --no-browser --allow-root --ip=172.17.0.2 --NotebookApp.token=

            From local web browser:

            .. code-block:: text

                Open COMPSs monitor: http://localhost:8080/compss-monitor/index.zul
                Open Jupyter notebook interface: http://localhost:8888/

        * Using **Virtual Machine**:

            * Download the OVA from: https://www.bsc.es/research-and-development/software-and-apps/software-list/comp-superscalar/downloads  (*Look for Virtual Appliances section*)
            * Import the OVA from VirtualBox
            * Start the Virtual Machine

                * User: **compss**
                * Password: **compss2019**

            * Open a console and run:

                .. code-block:: bash

                    $ git clone https://github.com/bsc-wdc/notebooks.git
                    $ cd notebooks
                    $ /etc/init.d/compss-monitor start
                    $ jupyter-notebook

            * Open the web browser:

                .. code-block:: text

                    * Open COMPSs monitor: http://localhost:8080/compss-monitor/index.zul
                    * Open Jupyter notebook interface: http://localhost:8888/


        * Using local installation

            * Get the notebooks and start jupyter

                .. code-block:: bash

                    $ git clone https://github.com/bsc-wdc/notebooks.git
                    $ cd notebooks
                    $ /etc/init.d/compss-monitor start
                    $ jupyter-notebook

            * Then

                .. code-block:: text

                    * Open COMPSs monitor: http://localhost:8080/compss-monitor/index.zul
                    * Open Jupyter notebook interface: http://localhost:8888/
                    * Look for the application.ipynb of interest.


    .. IMPORTANT::

        It is necessary to **RESTART the python kernel from Jupyter** after the execution of any notebook.


    Troubleshooting
        * ISSUE 1: Cannot connect using docker pull.

            REASON: *The docker service is not running*:

            .. code-block:: bash

                $ # Error messsage:
                $ Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
                $ # SOLUTION: Restart the docker service:
                $ sudo service docker start

        * ISSUE 2: The notebooks folder is empty or contains other data using docker.

            REASON: *The notebooks path in the docker run command is wrong*.

            .. code-block:: bash

                $ # Remove the docker instance and reinstantiate with the appropriate notebooks path
                $ exit
                $ docker stop mycompss
                $ docker rm mycompss
                $ # Pay attention and UPDATE: /PATH/TO in the next command
                $ docker run --name mycompss -p 8888:8888 -p 8080:8080 -v /PATH/TO/notebooks:/home/notebooks -itd compss/compss-tutorial:2.6
                $ # Continue as normal


        * ISSUE 3: COMPSs does not start in Jupyter.

            REASON: *The python kernel has not been restarted between COMPSs start, or some processes from previous failed execution may exist.*

            .. code-block:: bash

                $ # SOLUTION: Restart the python kernel from Jupyter and check that there are no COMPSs' python/java processes running.

        * ISSUE 4: Numba is not working with the VM or Docker.

            REASON: *Numba is not installed in the VM or docker*

            .. code-block:: bash

                $ # SOLUTION: Install Numba in the VM/Docker
                $ #           Open a console in the VM/Docker and follow the next steps.
                $ # For Python 2:
                $ sudo python2 -m pip install numba
                $ # For Python 3:
                $ sudo python3 -m pip install numba

        * ISSUE 5: Matplotlib is not working with the VM or Docker.

            REASON: *Matplotlib is not installed in the VM or docker*

            .. code-block:: bash

                $ # SOLUTION: Install Matplotlib in the VM/Docker
                $ #           Open a console in the VM/Docker and follow the next steps.
                $ # For Python 2:
                $ sudo python2 -m pip install matplotlib
                $ # For Python 3:
                $ sudo python3 -m pip install matplotlib

    Contact
        support-compss@bsc.es


.. |Binder| image:: https://mybinder.org/badge_logo.svg
    :alt: MyBinder
    :scale: 100%
    :target: https://mybinder.org/v2/gh/bsc-wdc/notebooks/master?urlpath=/tree/home/jovyan
