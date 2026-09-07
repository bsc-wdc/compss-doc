.. spelling:word-list::

   Conda
   Miniconda


Installation
************

There are three primary ways to install and start using PyCOMPSs:

1. Within a virtual environment (**RECOMMENDED**)
2. Using a Conda environment
3. Locally via pip

Choose the option that best suits your work flow.

🌟 **Option 1**: Virtual Environment (**RECOMMENDED**)
======================================================

To avoid conflicts with other Python packages, it is highly recommended to install `pycompss-cli` inside a virtual environment.

**On Linux/macOS:**

.. code-block:: console

  # Create the environment
  python3 -m venv pycompss-venv
  # Activate it
  source pycompss-venv/bin/activate
  # Install the package
  python3 -m pip install pycompss-cli

**On Windows:**

.. code-block:: console

  # Create the environment
  python -m venv pycompss-venv
  # Activate it
  .\pycompss-venv\Scripts\activate
  # Install the package
  pip install pycompss-cli

🐍 **Option 2**: Conda Environment
==================================

If you use Anaconda or Miniconda, you can create a dedicated environment to keep your dependencies isolated:

.. code-block:: console

  # Create a new conda environment with Python 3.10
  conda create -n pycompss-env python=3.10
  # Activate the environment
  conda activate pycompss-env
  # Install the package via pip
  python3 -m pip install pycompss-cli

⚡ **Option 3**: Local Installation
===================================

If you prefer a global installation across your system (Linux, macOS, and Windows):

.. code-block:: console

  python3 -m pip install pycompss-cli

Verify Installation
===================

To verify that the installation was successful, ensure that the `pycompss-cli` executables (``pycompss``, ``compss``, ``dislib``, and ``qdislib``, which are interchangeable) are available in your command line.

.. code-block:: console

   $ pycompss -h
   usage: pycompss [-h] [-d] [-i] [-v] [-p] [-s] [-g]
                {tutorial,tut,environment,env,status,envs,activate,use,default,reset,wipe,dep_check,dc,install,ins,exec,e,run,r,monitor,m,jupyter,n,gengraph,gg,gentrace,gt,inspect,i} ...

    ==============
    PyCOMPSs CLI
    ==============

    A command-line tool to develop and run COMPSs applications with ease.

    Run applications locally, in Docker, or on distributed infrastructures such as
    clusters and supercomputers. The CLI handles environment setup, job submission,
    and execution management for you.

    Built for usability and reproducibility, it streamlines parallel and distributed
    computing workflows using COMPSs.

    Resources:
    • COMPSs Website             : http://compss.bsc.es
    • COMPSs Repository          : https://github.com/bsc-wdc/compss
    • COMPSs Documentation       : https://compss.readthedocs.io/
    • pycompss-cli Documentation : https://compss.readthedocs.io/en/stable/Sections/04_Ecosystem/09_CLI.html

    Supported environments in this machine:
    ✔ local: Use local COMPSs installation.
    ✔ remote: Use a remote HPC COMPSs installation.
    ✘ docker: Docker environment NOT AVAILABLE.
        Install Docker and its Python bindings ('docker') in order to enable this environment type.
    ✘ unicore: UNICORE environment NOT AVAILABLE.
        Install 'pyunicore' in order to enable this environment type.

    Current environment:
    • Name : default
    • Type : local

    positional arguments:
    {tutorial,tut,environment,env,status,envs,activate,use,default,reset,wipe,dep_check,dc,install,ins,exec,e,run,r,monitor,m,jupyter,n,gengraph,gg,gentrace,gt,inspect,i}
        tutorial (tut)      Configure the environment for COMPSs training.
        environment (env)   Manage COMPSs environments.
        status (envs)       Show current COMPSs environment status (alias of 'environment list').
        activate (use)      Activate a COMPSs environment (alias of 'environment change').
        default             Change to 'default' environment (alias of 'environment change default').
        reset (wipe)        Remove all COMPSs environments (reset state).
                            Next actions will be applied using the current environment:
        dep_check (dc)      COMPSs dependency checker.
        install (ins)       COMPSs install.
        exec (e)            Execute command within COMPSs environment.
        run (r)             Run application (with runcompss).
        monitor (m)         Start/stop monitor.
        jupyter (n)         Start Jupyter notebook.
        gengraph (gg)       Convert graph to PDF.
        gentrace (gt)       Merge traces to Paraver trace.
        inspect (i)         Inspect RO-Crate(s) from a COMPSs application run.

    options:
    -h, --help            show this help message and exit
    -d, --debug           Enable debug mode.
    -i, --info            Enable info mode.
    -v, --version         Get version.
    -p, --plain           Plain mode (no color).
    -s, --sanitize        Avoid sensitive information in logs, out and err.
    -g, --gui             Graphical interface.