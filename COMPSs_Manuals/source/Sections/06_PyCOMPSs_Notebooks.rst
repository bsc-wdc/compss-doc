.. # define a hard line break for HTML
.. |br| raw:: html

   <br />

*****************************************************
|:notebook_with_decorative_cover:| PyCOMPSs Notebooks
*****************************************************

This section contains all PyCOMPSs related tutorial notebooks (sources available in https://github.com/bsc-wdc/notebooks).

It is divided into three main folders: |br|
* **Syntax**: Contains the main tutorial notebooks. They cover the syntax and main functionalities of PyCOMPSs. |br|
* **Hands-On**: Contains example applications and hands-on exercises. |br|
* **Demos**: Contains demonstration notebooks.


Syntax
######

Here you will find the PyCOMPSs programming model syntax notebooks used in the tutorials.

.. nbgallery::
    :name: syntax-nb-gallery

    06_PyCOMPSs_Notebooks/syntax/1_Basic
    06_PyCOMPSs_Notebooks/syntax/2_Synchronization
    06_PyCOMPSs_Notebooks/syntax/3.0_Defining_classes_and_objects
    06_PyCOMPSs_Notebooks/syntax/3.1_Defining_classes_and_objects-with-reduce
    06_PyCOMPSs_Notebooks/syntax/3.2_Defining_classes_and_objects-with-collections
    06_PyCOMPSs_Notebooks/syntax/3.3_Defining_classes_and_objects-with-dictionary
    06_PyCOMPSs_Notebooks/syntax/3.4_Defining_classes_and_objects-with-fault-tolerance
    06_PyCOMPSs_Notebooks/syntax/4_Files
    06_PyCOMPSs_Notebooks/syntax/5_UsingConstraints
    06_PyCOMPSs_Notebooks/syntax/6_Polymorphism
    06_PyCOMPSs_Notebooks/syntax/7_Binary
    06_PyCOMPSs_Notebooks/syntax/8_Integration_with_Numba
    06_PyCOMPSs_Notebooks/syntax/9_Dislib
    06_PyCOMPSs_Notebooks/syntax/10_Dislib_estimators


Hands-on
########

Here you will find the PyCOMPSs hands on notebooks used in the tutorials.

.. nbgallery::
    :name: handson-nb-gallery

    06_PyCOMPSs_Notebooks/hands-on/1_SortByKey
    06_PyCOMPSs_Notebooks/hands-on/2_KMeans
    06_PyCOMPSs_Notebooks/hands-on/2_KMeans-reduce-chunks
    06_PyCOMPSs_Notebooks/hands-on/3_Cholesky
    06_PyCOMPSs_Notebooks/hands-on/4_Wordcount_Exercise
    06_PyCOMPSs_Notebooks/hands-on/4_Wordcount_Solution
    06_PyCOMPSs_Notebooks/hands-on/4_Wordcount_Solution-with-reduce
    06_PyCOMPSs_Notebooks/hands-on/5_Integral_PI_iterative
    06_PyCOMPSs_Notebooks/hands-on/5_Integral_PI_reduction


Demos
#####

Here you will find the PyCOMPSs demonstration notebooks used in the tutorials.

.. nbgallery::
    :name: demos-nb-gallery

    06_PyCOMPSs_Notebooks/demos/Mandelbrot_numba



.. HINT::

    These notebooks can be used within **MyBinder**, with the **PyCOMPSs CLI**,
    within **Docker**, within **Virtual Machine** (recommended for Windows) provided by BSC, or locally.

    Prerequisites
        * Using *MyBinder*:

            * Open |Binder|

            .. CAUTION::

                Sometimes it may take a while to deploy the COMPSs infrastructure.

        * Using **PyCOMPSs CLI**:

            * ``pycompss-cli`` (see :ref:`Sections/04_Tools/09_CLI/01_Installation:Requirements and Installation`)

        * Using **Docker**:

            * Docker
            * Git

        * Using **Virtual Machine**:

            * VirtualBox

        * For **local** execution:

            * Python 3
            * Install COMPSs requirements described in :ref:`Sections/01_Installation_Configuration/01_Dependencies:Dependencies`.
            * Install COMPSs (See :ref:`install_from_sources`)
            * Jupyter (with the desired ipykernel)
            * ipywidgets (only for some hands-on notebooks)
            * numpy (only for some notebooks)
            * dislib (only for some notebooks)
            * numba (only for some notebooks)
            * Git

    Instructions
        * Using **MyBinder**:

            Just explore the folders and run the examples (they have the same structure as this documentation).

        * Using ``pycompss-cli``:

            Check the ``pycompss-cli`` usage instructions (see :ref:`Sections/04_Tools/09_CLI/02_Usage:Usage`)

            Get the notebooks:

            .. code-block:: bash

                $ git clone https://github.com/bsc-wdc/notebooks.git


        * Using **Docker**:

            Run in your machine:

            .. code-block:: bash

                $ git clone https://github.com/bsc-wdc/notebooks.git
                $ docker pull compss/compss-tutorial:latest
                $ # Update the path to the notebooks path in the next command before running it
                $ docker run --name mycompss -p 8888:8888 -p 8080:8080 -v /PATH/TO/notebooks:/home/notebooks -itd compss/compss-tutorial:latest
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
                $ docker run --name mycompss -p 8888:8888 -p 8080:8080 -v /PATH/TO/notebooks:/home/notebooks -itd compss/compss:3.3
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
    :target: https://mybinder.org/v2/gh/bsc-wdc/notebooks/master?urlpath=/tree/home/jovyan
