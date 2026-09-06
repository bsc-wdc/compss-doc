|:magic_wand:| CLI
##################

The PyCOMPSs CLI (``pycompss-cli``) provides a standalone tool to use PyCOMPSs
interactively within docker environments, local machines, remote clusters and UNICORE machines.
This tool has been implemented on top of the `PyCOMPSs programming model <http://compss.bsc.es>`__,
and it is being developed by the `Workflows and Distributed Computing
group <https://github.com/bsc-wdc>`__ of the `Barcelona Supercomputing
Center <https://www.bsc.es/>`__, and can be easily downloaded and installed
from the PyPI repository.

**Key Features:**

- **Multi-environment Support**: Manage multiple COMPSs environments (local, Docker, remote, UNICORE)
- **Dependency Management**: Automatic COMPSs dependency checking and installation
- **Application Execution**: Run PyCOMPSs applications with comprehensive control options
- **Monitoring**: Watch your application while executing
- **Inspection**: Inspect RO-Crate files for application execution analysis
- **Infrastructure Management**: Add/remove worker resources dynamically (Docker)
- **GUI Interface**: Graphical user interface for interactive application management

.. grid:: 1 1 1 1
    :gutter: 2

    .. grid-item-card:: Requirements
        :link: 09_CLI/01_Requirements
        :link-type: doc
        :text-align: center

        :material-twotone:`warning;3em`

    .. grid-item-card:: Installation
        :link: 09_CLI/02_Installation
        :link-type: doc
        :text-align: center

        :material-twotone:`install_desktop;3em`


.. grid:: 1 2 2 2
    :gutter: 2

    .. grid-item-card:: Command Line Interface
        :link: 09_CLI/03_Usage_CLI
        :link-type: doc
        :text-align: center

        :material-twotone:`terminal;3em`

    .. grid-item-card:: Graphical User Interface
        :link: 09_CLI/04_Usage_GUI
        :link-type: doc
        :text-align: center

        :material-twotone:`dashboard;3em`

.. toctree::
    :maxdepth: 3
    :caption: Table of Contents

    09_CLI/01_Requirements
    09_CLI/02_Installation
    09_CLI/03_Usage_CLI
    09_CLI/04_Usage_GUI