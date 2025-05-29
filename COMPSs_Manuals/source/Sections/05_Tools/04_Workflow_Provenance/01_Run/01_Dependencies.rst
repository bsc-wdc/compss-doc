---------------------
Software dependencies
---------------------

Provenance generation in COMPSs depends on the `ro-crate-py library <https://github.com/ResearchObject/ro-crate-py>`_,
thus, it must be installed before the provenance option can be used. Depending on the target system, different
options are available using ``pip``:

If the installation is in a laptop or machine you manage, you can use the command:

.. code-block:: console

    $ pip install rocrate

If you do not manage the target machine, you can install the library in your own user space using:

.. code-block:: console

    $ pip install rocrate --user

This would typically install the library in ``~/.local/``. Another option is to specify the target directory with:

.. code-block:: console

    $ pip install -t install_path rocrate

Our current implementation needs ``ro-crate-py`` version ``0.9.0`` or higher.

.. WARNING::

    If you are using a BSC cluster (MareNostrum, CTE-POWER, ...), ro-crate-py is already installed for a number of
    python versions at ``/apps/COMPSs/LIBRARIES/``, and COMPSs is configured to use it. Thus, you don't need
    to install ro-crate-py.

