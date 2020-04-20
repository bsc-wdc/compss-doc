Dependencies
============

Next we provide a list of dependencies for installing COMPSs package.
The exact names may vary depending on the Linux distribution but this
list provides a general overview of the COMPSs dependencies. For
specific information about your distribution please check the *Depends*
section at your package manager (apt, yum, zypper, etc.).

.. table:: COMPSs dependencies
    :name: COMPSs_dependencies
    :widths: auto

    +-------------------------+---------------------------------------------------------------------------------+
    | Module                  | Dependencies                                                                    |
    +=========================+=================================================================================+
    | **COMPSs Runtime**      | | **openjdk-8-jre, graphviz, xdg-utils, openssh-server**                        |
    +-------------------------+---------------------------------------------------------------------------------+
    | COMPSs Python Binding   | | libtool, automake, build-essential, python (>= 2.7 \| >=3.5),                 |
    |                         | | python-dev \| python3-dev, python-setuptools\|python3-setuptools,             |
    |                         | | libpython2.7                                                                  |
    +-------------------------+---------------------------------------------------------------------------------+
    | COMPSs C/C++ Binding    | | libtool, automake, build-essential, libboost-all-dev, libxml2-dev             |
    +-------------------------+---------------------------------------------------------------------------------+
    | COMPSs Autoparallel     | | libgmp3-dev, flex, bison, libbison-dev, texinfo, libffi-dev, astor,           |
    |                         | | sympy, enum34, islpy                                                          |
    +-------------------------+---------------------------------------------------------------------------------+
    | COMPSs Tracing          | | libxml2 (>= 2.5), libxml2-dev (>= 2.5), gfortran, papi                        |
    +-------------------------+---------------------------------------------------------------------------------+


Build Dependencies
------------------

To build COMPSs from sources you will also need ``wget``,
``openjdk-8-jdk`` and ``maven``.

Optional Dependencies
---------------------

For the Python binding it is also recommended to have ``dill`` and
``guppy`` installed. The ``dill`` package increases the variety of
serializable objects by Python (for example: lambda functions), and the
``guppy`` package is needed to use the ``@local`` decorator. Both
packages can be found in pyPI and can be installed via ``pip``.
