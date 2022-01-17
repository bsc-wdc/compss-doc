Install COMPSs
--------------

* Choose the installation method:

.. content-tabs::

    .. tab-container:: Local
        :title: Pip - Local to the user

        |
        | **Requirements:**
        |
        | - Ensure that the required system :ref:`Sections/01_Installation/01_Dependencies:Dependencies` are installed.
        | - Check that your ``JAVA_HOME`` environment variable points to the Java JDK folder, that the ``GRADLE_HOME`` environment variable points to the GRADLE folder, and the ``gradle`` binary is in the ``PATH`` environment variable.
        | - Enable SSH passwordless to localhost. See :ref:`Sections/01_Installation/05_Additional_configuration:Configure SSH passwordless`.
        |
        | COMPSs will be installed within the ``$HOME/.local/`` folder (or alternatively within the active virtual environment).
        |

           .. code-block:: console

               $ pip install pycompss -v

           .. important::

               Please, update the environment after installing COMPSs:

               .. code-block:: console

                  $ source ~/.bashrc  # or alternatively reboot the machine

               If installed within a virtual environment, deactivate and activate
               it to ensure that the environment is propperly updated.

               .. WARNING::

                   If using Ubuntu 18.04 or higher, you will need to comment
                   some lines of your ``.bashrc`` and do a complete logout.
                   Please, check the :ref:`Sections/01_Installation/02_Building_from_sources:Post installation`
                   Section for detailed instructions.

        | See :ref:`Sections/01_Installation:Installation and Administration` section for more information
        |

    .. tab-container:: Systemwide
        :title: Pip - Systemwide

        |
        | **Requirements:**
        |
        | - Ensure that the required system :ref:`Sections/01_Installation/01_Dependencies:Dependencies` are installed.
        | - Check that your ``JAVA_HOME`` environment variable points to the Java JDK folder, that the ``GRADLE_HOME`` environment variable points to the GRADLE folder, and the ``gradle`` binary is in the ``PATH`` environment variable.
        | - Enable SSH passwordless to localhost. See :ref:`Sections/01_Installation/05_Additional_configuration:Configure SSH passwordless`.
        |
        | COMPSs will be installed within the ``/usr/lib64/pythonX.Y/site-packages/pycompss/`` folder.
        |

           .. code-block:: console

               $ sudo -E pip install pycompss -v

           .. important::

               Please, update the environment after installing COMPSs:

               .. code-block:: console

                   $ source /etc/profile.d/compss.sh  # or alternatively reboot the machine

               .. WARNING::

                   If using Ubuntu 18.04 or higher, you will need to comment
                   some lines of your ``.bashrc`` and do a complete logout.
                   Please, check the :ref:`Sections/01_Installation/02_Building_from_sources:Post installation`
                   Section for detailed instructions.

        | See :ref:`Sections/01_Installation:Installation and Administration` section for more information
        |

    .. tab-container:: SourcesLocal
        :title: Build from sources - Local to the user

        |
        | **Requirements:**
        |
        | - Ensure that the required system :ref:`Sections/01_Installation/01_Dependencies:Dependencies` are installed.
        | - Check that your ``JAVA_HOME`` environment variable points to the Java JDK folder, that the ``GRADLE_HOME`` environment variable points to the GRADLE folder, and the ``gradle`` binary is in the ``PATH`` environment variable.
        | - Enable SSH passwordless to localhost. See :ref:`Sections/01_Installation/05_Additional_configuration:Configure SSH passwordless`.
        |
        | COMPSs will be installed within the ``$HOME/COMPSs/`` folder.
        |

           .. code-block:: console

               $ git clone https://github.com/bsc-wdc/compss.git
               $ cd compss
               $ ./submodules_get.sh
               $ ./submodules_patch.sh
               $ cd builders/
               $ export INSTALL_DIR=$HOME/COMPSs/
               $ ./buildlocal ${INSTALL_DIR}

        | The different installation options can be found in the command help.

           .. code-block:: console

               $ ./buildlocal -h

        | Please, check the :ref:`Sections/01_Installation/02_Building_from_sources:Post installation` Section.

        | See :ref:`Sections/01_Installation:Installation and Administration` section for more information
        |

    .. tab-container:: SourcesSystemwide
        :title: Build from sources - Systemwide

        |
        | **Requirements:**
        |
        | - Ensure that the required system :ref:`Sections/01_Installation/01_Dependencies:Dependencies` are installed.
        | - Check that your ``JAVA_HOME`` environment variable points to the Java JDK folder, that the ``GRADLE_HOME`` environment variable points to the GRADLE folder, and the ``gradle`` binary is in the ``PATH`` environment variable.
        | - Enable SSH passwordless to localhost. See :ref:`Sections/01_Installation/05_Additional_configuration:Configure SSH passwordless`.
        |
        | COMPSs will be installed within the ``/opt/COMPSs/`` folder.
        |

           .. code-block:: console

               $ git clone https://github.com/bsc-wdc/compss.git
               $ cd compss
               $ ./submodules_get.sh
               $ ./submodules_patch.sh
               $ cd builders/
               $ export INSTALL_DIR=/opt/COMPSs/
               $ sudo -E ./buildlocal ${INSTALL_DIR}

        | The different installation options can be found in the command help.

           .. code-block:: console

               $ ./buildlocal -h

        | Please, check the :ref:`Sections/01_Installation/02_Building_from_sources:Post installation` Section.

        | See :ref:`Sections/01_Installation:Installation and Administration` section for more information
        |

    .. tab-container:: Supercomputer
        :title: Supercomputer

        |
        | Please, check the :ref:`Sections/01_Installation/04_Supercomputers:Supercomputers` section.
        |

    .. tab-container:: Docker
        :title: Docker - PyCOMPSs CLI

        |
        | **Requirements (Optional):**
        |
        | - `docker <https://www.docker.com>`_ >= 17.12.0-ce
        | - Python 3
        | - pip
        | - `docker package for Python <https://pypi.org/project/docker/>`_
        |
        | Since the PyCOMPSs CLI package is available in Pypi (`pycompss-cli <https://pypi.org/project/pycompss-cli/>`_), it can be easly installed with ``pip`` as follows:
        |

          .. code-block:: console

              $ python3 -m pip install pycompss-cli

        |
        | A complete guide about the PyCOMPSs CLI installation and usage can be found in the :ref:`Sections/08_PyCOMPSs_CLI:PyCOMPSs CLI` Section.
        |

          .. TIP::

              Please, check the PyCOMPSs CLI :ref:`Sections/08_PyCOMPSs_CLI/01_Installation:Installation` Section for the further information with regard to the requirements installation and troubleshooting.
