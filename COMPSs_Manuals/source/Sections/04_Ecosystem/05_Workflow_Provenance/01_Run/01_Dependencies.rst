Software dependencies
=====================

Provenance generation in COMPSs relies on a set of Python packages. Some of them are **mandatory**: if any of them
is missing, the workflow provenance generation fails.
Others are **recommended**: if they are missing, the crate is still generated, but some of its contents
(e.g. the resource usage information or the profiling plots) are skipped, and a warning is printed.

Mandatory packages
------------------

- ``rocrate`` (the `ro-crate-py library <https://github.com/ResearchObject/ro-crate-py>`_), version ``0.13.0`` or
  higher. It is used to build and write the RO-Crate.
- ``pyyaml``, to read the YAML configuration file.
- ``pytz``, to record the times of the run.
- ``requests``, for the automatic search of Authors and Agent details (see Section :ref:`yaml-config`).

Depending on the target system, different options are available to install them using ``pip``.
If the installation is in a laptop or machine you manage, you can use the command:

.. code-block:: console

    $ pip install rocrate pyyaml pytz requests

If you do not manage the target machine, you can install the libraries in your own user space using:

.. code-block:: console

    $ pip install rocrate pyyaml pytz requests --user

This would typically install the libraries in ``~/.local/``. Another option is to specify the target directory with:

.. code-block:: console

    $ pip install -t install_path rocrate pyyaml pytz requests

.. WARNING::

    If you are using a BSC cluster (e.g. MareNostrum 5), ro-crate-py is already installed for a number of
    python versions at ``/apps/COMPSs/LIBRARIES/``, and COMPSs is configured to use it. Thus, you don't need
    to install ro-crate-py.

.. TIP::

    If you installed the COMPSs CLI (:ref:`Sections/04_Ecosystem/09_CLI:|:magic_wand:| CLI`),
    the ro-crate-py library dependency will have been already solved, since the CLI also relies
    on ro-crate-py to open and process crates.

Recommended packages
--------------------

- ``pandas``, to add the resource usage of each node (from the profiling ``csv`` files) to the
  metadata, and to generate the profiling plots.
- ``matplotlib``, to generate the profiling plots of the ``profiling/`` folder of the crate (see Section
  :ref:`resulting-crate`). Both ``pandas`` and ``matplotlib`` are needed by the ``compss_genprofiling`` tool that
  draws the plots: if any of them is missing, the plots are not included in the crate.
- ``psutil``, **only on macOS**. The resource usage profiler that is automatically activated with provenance needs it,
  since the ``/proc`` directory is not available. If it is not installed, the profiler stops with the error
  ``PROVENANCE | PROFILING | ERROR: psutil is required on macOS for CPU/memory profiling``, and no resource usage
  information is recorded for the run.

They can be installed with the same ``pip`` options described above (``psutil`` is only needed on macOS):

.. code-block:: console

    $ pip install pandas matplotlib psutil

.. WARNING::

    In COMPSs versions from ``3.3.3.post2511`` up to ``3.4.post2610``, the workflow provenance generation fails completely
    (``PROVENANCE | WORKFLOW PROVENANCE GENERATION HAS FAILED``) if ``pandas`` is not installed. Make sure to
    install it when using those versions.
