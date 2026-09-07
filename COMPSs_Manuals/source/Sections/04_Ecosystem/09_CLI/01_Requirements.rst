Requirements
************

Minimal Requirements
====================

- Python >= 3.10
- Linux, MacOS, or Windows.

Optional Requirements
=====================

The CLI supports various COMPSs installed environments. Depending on the environment type, additional requirements may apply.

Local environments
------------------

- Linux or MacOS

.. CAUTION::
  ⚠️ **Windows users**: COMPSs does not provide native support for Windows. Please use **WSL** (Windows Subsystem for Linux) to enable local environment usage.

Remote environments (HPC)
-------------------------

- Internet connectivity
- Access to the remote machine

Dockerized environments
-----------------------

To run and deploy Docker-based environments, the following installations are required:

- `docker <https://www.docker.com>`_
- `docker package <https://pypi.org/project/docker/>`_ for Python

.. content-tabs::

   .. tab-container:: Linux
        :title: Linux

          1. **Install Docker** (skip this step if already installed):

             - Suggested installation instructions:
                - `Docker for Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1>`__.
                - `Docker for Arch Linux <https://wiki.archlinux.org/index.php/Docker#Installation>`__.
             - **Note**: In some distributions, the Docker package has been renamed from ``docker`` to ``docker-ce``. Ensure you install the correct package.

          2. **Configure permissions**: Add the user to the docker group to run containers as a non-root user:

             - `Instructions <https://docs.docker.com/install/linux/linux-postinstall/>`__

          3. **Verify installation**:

             .. code-block:: console

                 $ docker --version
                 $ docker ps # this should be empty as no docker processes are yet running.

          4. **Install the Python docker library**:

             .. code-block:: console

                 $ python3 -m pip install docker

             .. TIP::

                 Some Linux distributions do not include the ``$HOME/.local/bin`` folder in the ``PATH`` environment variable, preventing access to the ``pycompss-cli`` commands (and any other Python packages installed in the user HOME). If the ``pycompss``, ``compss``, or ``dislib`` commands are not recognized after installation, add the following line to your ``.bashrc`` and refresh your current session:

                 .. code-block:: console

                     $ export PATH=${HOME}/.local/bin:${PATH}

   .. tab-container:: MacOS
        :title: MacOS

          1. **Install Docker** (skip this step if already installed):

             - Suggested installation instructions:
                - `Docker for Mac <https://store.docker.com/editions/community/docker-ce-desktop-mac>`__.
                - Alternatively, use `Homebrew <https://brew.sh/>`__.

          2. **Configure permissions**: Add the user to the docker group to run containers as a non-root user:

             - `Instructions <https://docs.docker.com/install/linux/linux-postinstall/>`__

          3. **Verify installation**:

             .. code-block:: console
                 $ docker --version
                 $ docker ps # this should be empty as no docker processes are yet running.

          4. **Install the Python docker library**:

             .. code-block:: console
                 $ python3 -m pip install docker

             .. TIP::

                 If the ``pycompss``, ``compss``, ``dislib``, or ``qdislib`` commands are not recognized after installation, you may need to include the following line in your ``.bashrc`` or ``.zshrc`` and refresh your current session:

                 .. code-block:: console

                     $ export PATH=${HOME}/.local/bin:${PATH}

   .. tab-container:: Windows
        :title: Windows

          1. **Install Docker** (skip this step if already installed):

             - Suggested installation instructions:
               - `Docker for Windows <https://docs.docker.com/desktop/windows/install/>`__.

          2. **Verify installation**:

             .. code-block:: console

                 $ docker --version
                 $ docker ps # this should be empty as no docker processes are yet running.

          3. **Install the Python docker library**:

             .. code-block:: console

                 $  python3 -m pip install docker

UNICORE environments
--------------------

- `pyunicore package <https://pypi.org/project/pyunicore/>`_

Installing `pyunicore <https://github.com/HumanBrainProject/pyunicore>`__ for Python is required for running and deploying UNICORE-type environments.

.. code-block:: console

   $  python3 -m pip install pyunicore