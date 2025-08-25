.. tab-set::

    .. tab-item:: Tumbleweed

        **OpenSuse Tumbleweed** dependencies installation commands:

        .. literalinclude:: ./01_PC/01_Linux/02_OpenSuse/COMPSs_deps_OpenSuse_Tumbleweed.sh
            :language: bash

        :download:`this example script <./01_PC/01_Linux/02_OpenSuse/COMPSs_deps_OpenSuse_Tumbleweed.sh>`

    .. tab-item:: Leap 15.X

        **OpenSuse Leap 15.X** dependencies installation commands:

        .. literalinclude:: ./01_PC/01_Linux/02_OpenSuse/COMPSs_deps_OpenSuse_15_X.sh
            :language: bash

        :download:`this example script <./01_PC/01_Linux/02_OpenSuse/COMPSs_deps_OpenSuse_15_X.sh>`

    .. tab-item:: 42.2

        **OpenSuse 42.2** dependencies installation commands:

        .. literalinclude:: ./01_PC/01_Linux/02_OpenSuse/COMPSs_deps_OpenSuse_42_2.sh
            :language: bash

        :download:`this example script <./01_PC/01_Linux/02_OpenSuse/COMPSs_deps_OpenSuse_42_2.sh>`

        .. WARNING::

            OpenSuse provides Python 3.4 from its repositories, which is not supported
            by the COMPSs python binding.
            Please, update Python 3 (``python`` and ``python-devel``) to a higher
            version if you expect to install COMPSs from sources.

            Alternatively, you can use a virtual environment.

    .. tab-item:: Other

        .. include:: ./03_General/03_version_email_inc.rst