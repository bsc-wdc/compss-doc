Software dependencies
=====================

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

Our current implementation needs ``ro-crate-py`` version ``0.13.0`` or higher.

.. WARNING::

    If you are using a BSC cluster (MareNostrum, CTE-POWER, ...), ro-crate-py is already installed for a number of
    python versions at ``/apps/COMPSs/LIBRARIES/``, and COMPSs is configured to use it. Thus, you don't need
    to install ro-crate-py.

.. WARNING::

    Some Python versions at some Linux distributions do not have installed by default ``yaml``, ``pytz`` and
    ``requests`` (used for the automatic search of Authors and Agent details, see Section :ref:`yaml-config`), thus
    you will need to install them too using ``pip``.

Besides, the ``pandas`` package is recommended. It is used to add the resource usage of each node (from the profiling
``csv`` files) and the energy data to the metadata, and to generate the profiling plots. If it is not installed,
these parts are skipped and a warning is printed:

.. code-block:: console

    $ pip install pandas

.. WARNING::

    In COMPSs versions from ``3.3.3.post2511`` up to ``3.4.post2610``, the workflow provenance generation fails completely
    (``PROVENANCE | WORKFLOW PROVENANCE GENERATION HAS FAILED``) if ``pandas`` is not installed. Make sure to
    install it when using those versions.

.. TIP::

    If you installed the COMPSs CLI (:ref:`Sections/04_Ecosystem/09_CLI:|:magic_wand:| CLI`),
    the ro-crate-py library dependency will have been already solved, since the CLI also relies
    on ro-crate-py to open and process crates.