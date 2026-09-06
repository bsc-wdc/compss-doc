Installation
************

You can start using PyCOMPSs in three ways:

1. Install within a virtual environment (**RECOMMENDED**)
2. Install locally via pip
3. Use Docker-based environments

Choose the one that best suits you.

🌟 **Option 1**: Virtual Environment (**RECOMMENDED**)
======================================================


To avoid conflicts with other Python packages, it is highly recommended to install `pycompss-cli` inside a virtual environment:

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


⚡ **Option 2**: Local Installation
===================================


If you prefer a global installation (Linux, macOS, and Windows):

.. code-block:: console

  python3 -m pip install pycompss-cli


.. 🐳 **Option 3**: Docker-based Environment
.. =========================================


.. If you prefer to run the CLI inside a pre-configured container:

.. .. code-block:: console

..   ./start_container.sh


.. .. WARNING::

..    ⚠️ **Windows users**: Please use **WSL** to run the `.sh` script.



Check installation
==================

In order to check that it is correctly installed, check that the
pycompss-cli executables (``pycompss``, ``compss``, ``dislib`` and ``qdislib``,
which can be used indifferently) are available from your command line.

.. code-block:: console

   $ pycompss -h
   [PyCOMPSs CLI options will be shown]
