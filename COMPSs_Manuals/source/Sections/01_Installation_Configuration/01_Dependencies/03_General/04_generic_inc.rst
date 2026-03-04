.. spelling:word-list::

   pre

The following table provides a list of dependencies for installing COMPSs package.

The exact names may vary depending on the Linux/macOS distribution but this
list provides a general overview of the COMPSs dependencies. For
specific information about your distribution please check the *Depends*
section at your package manager (apt, yum, zypper, etc.).

.. table:: COMPSs dependencies
    :name: COMPSs_dependencies

    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | Module                  | Dependencies                                                                                                                                 |
    +=========================+==============================================================================================================================================+
    | COMPSs Runtime          | openjdk-11-jdk (or JRE if using the pre-built runtime), graphviz, xdg-utils, openssh-server, gradle (8.7)                                    |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | COMPSs Python Binding   | libtool, automake, build-essential, python (>=3.7), python3-dev, python3-setuptools (>=61.0.0)                                               |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | COMPSs C/C++ Binding    | libtool, automake, build-essential, libboost-all-dev, libxml2-dev                                                                            |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | COMPSs R Binding        | build-essential, R (>=3.6.3)                                                                                                                 |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | COMPSs Tracing          | libxml2 (>= 2.5), libxml2-dev (>= 2.5), gfortran, papi                                                                                       |
    +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
