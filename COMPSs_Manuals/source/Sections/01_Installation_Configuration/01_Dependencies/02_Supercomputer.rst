.. spelling:word-list::

   pre

Supercomputer
*************

This section shows you the pre-requisites to install the COMPSs framework.
There are 3 types:

 * *Essential*: Minimal packages to install COMPSs.
 * *Build*: Extra packages to build COMPSs from sources.
 * *Optional*: Extra packages recommended for performance purposes.

Essential Requirements
======================

There are some systemwide packages required in order to install COMPSs.


Build Dependencies
==================

To build COMPSs from sources you will also need ``wget``, ``git`` and
``maven`` (`maven web <https://maven.apache.org/>`_).
To install with Pip, ``pip`` for the target Python version is required.


Optional Dependencies
=====================

For the Python binding it is recommended to have ``dill`` (`dill project <https://pypi.org/project/dill/>`_),
``guppy3`` (`guppy3 project <https://pypi.org/project/guppy3/>`_) and
``numpy`` (`numpy project <https://pypi.org/project/numpy/>`_) installed:

* The ``dill`` package increases the variety of serializable objects by Python (for example: lambda functions)
* The ``guppy3`` package is needed to use the ``@local`` decorator.
* The ``numpy`` package is useful to improve the serialization/deserialization performance since its internal mechanisms are used by the Python binding.

These packages can be found in PyPI and can be installed via ``pip``.

Since it is possible to execute python applications using workers spawning
MPI processes instead of multiprocessing, it is necessary to have ``openmpi``,
``openmpi-devel`` and ``openmpi-libs`` system packages installed and ``mpi4py`` with pip.

.. CAUTION::

    The ``mpi4py`` package requires to have the MPI header/development package available,
    which has to be installed with the OS package manager.

    .. code-block:: console

        $ sudo apt-get install libopenmpi-dev  # Adapt for your OS package manager
