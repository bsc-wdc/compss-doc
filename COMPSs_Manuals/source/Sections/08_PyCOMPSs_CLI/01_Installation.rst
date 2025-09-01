Requirements and Installation
=============================

Requirements
------------

- Python 3

Optional Requirements
^^^^^^^^^^^^^^^^^^^^^

- `docker <https://www.docker.com>`_
- `docker package <https://pypi.org/project/docker/>`_ for Python


Installation
------------

1. Install `pycompss-cli <https://pypi.org/project/pycompss-cli/>`_:

   Since the PyCOMPSs CLI package is available in PyPI, it can be easily installed with ``pip`` as follows:

   .. code-block:: console

      $ python3 -m pip install pycompss-cli


2. Check the `pycompss-cli <https://pypi.org/project/pycompss-cli/>`_ installation:

   In order to check that it is correctly installed, check that the
   pycompss-cli executables (``pycompss``, ``compss`` and ``dislib``,
   which can be used indifferently) are available from your command line.

   .. code-block:: console

      $ pycompss
      [PyCOMPSs CLI options will be shown]

Installing docker is optional and it's only required for running and deploying Docker type
environments.

.. content-tabs::

   .. tab-container:: Unix
        :title: Unix

          2. Install Docker (continue with step 3 if already installed):

             2.1. Suggested Docker installation instructions:

                -  `Docker for
                   Mac <https://store.docker.com/editions/community/docker-ce-desktop-mac>`__.
                   Or, if you prefer to use `Homebrew <https://brew.sh/>`__.

                -  `Docker for
                   Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1>`__.

                -  `Docker for Arch
                   Linux <https://wiki.archlinux.org/index.php/Docker#Installation>`__.

                Be aware that for some distributions the Docker package has been renamed
                from ``docker`` to ``docker-ce``. Make sure you install the new
                package.

             2.2. Add user to docker group to run the containers as a non-root user:

                -  `Instructions <https://docs.docker.com/install/linux/linux-postinstall/>`__

             2.3. Check that docker is correctly installed:

                 .. code:: bash

                     $ docker --version
                     $ docker ps # this should be empty as no docker processes are yet running.

          3. Install `docker <https://docker-py.readthedocs.io/en/stable/>`__ for python:

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
   .. tab-container:: Windows
        :title: Windows

         1. Install Docker (continue with step 2 if already installed):

             2.1. Suggested Docker installation instructions:

               - `Docker for Windows <https://docs.docker.com/desktop/windows/install/>`__.

             2.2. Check that docker is correctly installed:

                 .. code:: bash

                     $ docker --version
                     $ docker ps # this should be empty as no docker processes are yet running.

         2. Install `docker-py <https://docker-py.readthedocs.io/en/stable/>`__ for python:

             .. code:: bash

                 $  python3 -m pip install docker
