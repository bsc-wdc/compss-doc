Installation
============

Requirements
------------

- Python 3
- `docker <https://www.docker.com>`_ >= 17.12.0-ce
- `docker <https://pypi.org/project/docker-py/>`_ for python


Installation
------------

1. Install Docker (continue with step 2 if already installed):

   1.1. Suggested Docker installation instructions:

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

   1.2. Add user to docker group to run the containers as a non-root user:

      -  `Instructions <https://docs.docker.com/install/linux/linux-postinstall/>`__

   1.3. Check that docker is correctly installed:

       .. code:: bash

           $ docker --version
           $ docker ps # this should be empty as no docker processes are yet running.

2. Install `docker <https://docker-py.readthedocs.io/en/stable/>`__ for python
   (continue with step 3 if already installed):

   .. code:: bash

       $ python3 -m pip install docker

3. Install `pycompss-player <https://pypi.org/project/pycompss-player/>`_:

   Since the PyCOMPSs playerpackage is available in Pypi, it can be easly installed with ``pip`` as follows:

   .. code-block:: console

       $ python3 -m pip install pycompss-player


4. Check the `pycompss-player <https://pypi.org/project/pycompss-player/>`_ installation:

   In order to check that it is correctly installed, check that the
   pycompss-player executables (``pycompss``, ``compss`` and ``dislib``,
   which can be used indiferently) are available from your command line.

   .. code-block:: console

       $ pycompss
       [PyCOMPSs player options will be shown]


   .. TIP::

       Some Linux distributions do not include the ``$HOME/.local/bin`` folder
       in the ``PATH`` environment variable, preventing to access to the ``pycompss-player``
       commands (and any other Python packages installed in the user HOME).

       If you experience that the ``pycompss``\| ``compss``\|``dislib`` command is
       not available after the installation, you may need to include the
       following line into your ``.bashrc`` and execute it in your current session:

       .. code-block:: console

           $ export PATH=${HOME}/.local/bin:${PATH}
