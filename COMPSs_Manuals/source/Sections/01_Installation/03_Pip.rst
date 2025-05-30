Pip
===

Prerequisites
-------------

In order to be able to install COMPSs and PyCOMPSs with Pip, the
dependencies (excluding the COMPSs packages) mentioned
in the :ref:`Sections/01_Installation/01_Dependencies:Dependencies` Section must be satisfied (*do not forget*
to have proper ``JAVA_HOME`` and ``GRADLE_HOME`` environment variables pointing to the
Java JDK folder and Gradle home respectively, as well as the ``gradle`` binary in the
``PATH`` environment variable) and Python ``pip``.

Installation
------------

Depending on the machine, the installation command may vary. Some of the
possible scenarios and their proper installation command are:


.. tabs::

    .. tab:: Install systemwide

        Install system-wide:

        .. code-block:: console

            $ sudo -E pip install pycompss -v

        .. ATTENTION::

            Root access is required.

        It is recommended to restart the user session once the installation
        process has finished. Alternatively, the following command sets all
        the COMPSs environment in the current session.

        .. code-block:: console

            $ source /etc/profile.d/compss.sh

    .. tab:: Install in user local folder

        Install in user home folder (.local):

        .. code-block:: console

            $ pip install pycompss -v

        It is recommended to restart the user session once the installation
        process has finished. Alternatively, the following command sets all
        the COMPSs environment.

        .. code-block:: console

            $ source ~/.bashrc

    .. tab:: Within a virtual environment

        Within a Python virtual environment:

        .. code-block:: console

            (virtualenv) $ pip install pycompss -v

        In this particular case, the installation includes the necessary
        variables in the activate script. So, restart the virtual environment
        in order to set all the COMPSs environment.


Post installation
-----------------

If you need to set up your machine for the first time please take a look
at :ref:`Sections/01_Installation/05_Additional_configuration:Additional Configuration`
Section for a detailed description of the additional configuration.
