Requirements
************

Minimal Requirements
====================

- Python >= 3.10

- Linux, MacOS or Windows.


Optional Requirements
=====================

The CLI is capable of working with various COMPSs installed environments. However, there are some
requirements in order to manage them.

Local environments
------------------

- Linux or MacOS

.. CAUTION::

  ⚠️ **Windows users**: COMPSs does not provide native support for Windows. Please use **WSL** to
  install enable the local environment usage.

Remote environments (HPC)
-------------------------

- Internet connectivity
- Access to the remote machine

Dockerized environments
-----------------------

Installing docker is required for running and deploying Docker type environments:

- `docker <https://www.docker.com>`_
- `docker package <https://pypi.org/project/docker/>`_ for Python

.. content-tabs::

   .. tab-container:: Linux
        :title: Linux

          3. Install Docker (continue with step 3 if already installed):

             3.1. Suggested Docker installation instructions:

                -  `Docker for
                   Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1>`__.

                -  `Docker for Arch
                   Linux <https://wiki.archlinux.org/index.php/Docker#Installation>`__.

                Be aware that for some distributions the Docker package has been renamed
                from ``docker`` to ``docker-ce``. Make sure you install the new
                package.

             3.2. Add user to docker group to run the containers as a non-root user:

                -  `Instructions <https://docs.docker.com/install/linux/linux-postinstall/>`__

             3.3. Check that docker is correctly installed:

                 .. code:: bash

                     $ docker --version
                     $ docker ps # this should be empty as no docker processes are yet running.

          4. Install `docker <https://docker-py.readthedocs.io/en/stable/>`__ for python:

             .. code:: bash

                 $ python3 -m pip install docker


             .. TIP::

                 Some Linux distributions do not include the ``$HOME/.local/bin`` folder
                 in the ``PATH`` environment variable, preventing to access to the ``pycompss-cli``
                 commands (and any other Python packages installed in the user HOME).

                 If you experience that the ``pycompss``\| ``compss``\| ``dislib`` command is
                 not available after the installation, you may need to include the
                 following line into your ``.bashrc`` and execute it in your current session:

                 .. code-block:: console

                     $ export PATH=${HOME}/.local/bin:${PATH}

   .. tab-container:: MacOS
        :title: MacOS

          3. Install Docker (continue with step 3 if already installed):

             3.1. Suggested Docker installation instructions:

                -  `Docker for
                   Mac <https://store.docker.com/editions/community/docker-ce-desktop-mac>`__.
                   Or, if you prefer to use `Homebrew <https://brew.sh/>`__.

             3.2. Add user to docker group to run the containers as a non-root user:

                -  `Instructions <https://docs.docker.com/install/linux/linux-postinstall/>`__

             3.3. Check that docker is correctly installed:

                 .. code:: bash

                     $ docker --version
                     $ docker ps # this should be empty as no docker processes are yet running.

          4. Install `docker <https://docker-py.readthedocs.io/en/stable/>`__ for python:

             .. code:: bash

                 $ python3 -m pip install docker


             .. TIP::

                 If you experience that the ``pycompss``\| ``compss``\| ``dislib``\| ``qdislib`` command is
                 not available after the installation, you may need to include the
                 following line into your ``.bashrc`` and execute it in your current session:

                 .. code-block:: console

                     $ export PATH=${HOME}/.local/bin:${PATH}

   .. tab-container:: Windows
        :title: Windows

         3. Install Docker (continue with step 2 if already installed):

             3.1. Suggested Docker installation instructions:

               - `Docker for Windows <https://docs.docker.com/desktop/windows/install/>`__.

             3.2. Check that docker is correctly installed:

                 .. code:: bash

                     $ docker --version
                     $ docker ps # this should be empty as no docker processes are yet running.

         4. Install `docker-py <https://docker-py.readthedocs.io/en/stable/>`__ for python:

             .. code:: bash

                 $  python3 -m pip install docker

UNICORE environments
--------------------

  - `pyunicore package <https://pypi.org/project/pyunicore/>`_

  Installing `pyunicore <https://github.com/HumanBrainProject/pyunicore>`__ for python is required for
  running and deploying UNICORE type environments.

  .. code:: bash

     $  python3 -m pip install pyunicore
