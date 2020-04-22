.. |br| raw:: html

   <br />

Quickstart
==========

Install COMPSs
--------------

* Choose the installation method:

.. content-tabs::

    .. tab-container:: Local
        :title: Pip - Local to the user

        |
        | **Requirements:**
        |
        | - Ensure that the required system :ref:`Dependencies` are installed.
        | - Check that your ``JAVA_HOME`` points to the Java JDK folder.
        | - Enable SSH passwordless to localhost. See :ref:`Configure SSH passwordless`.
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

        | See :ref:`Installation and Administration` section for more information
        |

    .. tab-container:: Systemwide
        :title: Pip - Systemwide

        |
        | **Requirements:**
        |
        | - Ensure that the required system :ref:`Dependencies` are installed.
        | - Check that your ``JAVA_HOME`` points to the Java JDK folder.
        | - Enable SSH passwordless to localhost. See :ref:`Configure SSH passwordless`.
        |
        | COMPSs will be installed within the ``/usr/lib64/pythonX.Y/site-packages/pycompss/`` folder.
        |

           .. code-block:: console

               $ sudo -E pip install pycompss -v

           .. important::
               Please, update the environment after installing COMPSs:

               .. code-block:: console

                   $ source /etc/profile.d/compss.sh  # or alternatively reboot the machine

        | See :ref:`Installation and Administration` section for more information
        |

    .. tab-container:: SourcesLocal
        :title: Build from sources - Local to the user

        |
        | **Requirements:**
        |
        | - Ensure that the required system :ref:`Dependencies` are installed.
        | - Check that your ``JAVA_HOME`` points to the Java JDK folder.
        | - Enable SSH passwordless to localhost. See :ref:`Configure SSH passwordless`.
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
               $ ./buildlocal [options] ${INSTALL_DIR}

        | The different installation options can be found in the command help.

           .. code-block:: console

               $ ./buildlocal -h

        | See :ref:`Installation and Administration` section for more information
        |

    .. tab-container:: SourcesSystemwide
        :title: Build from sources - Systemwide

        |
        | **Requirements:**
        |
        | - Ensure that the required system :ref:`Dependencies` are installed.
        | - Check that your ``JAVA_HOME`` points to the Java JDK folder.
        | - Enable SSH passwordless to localhost. See :ref:`Configure SSH passwordless`.
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
               $ sudo -E ./buildlocal [options] ${INSTALL_DIR}

        | The different installation options can be found in the command help.

           .. code-block:: console

               $ ./buildlocal -h

        | See :ref:`Installation and Administration` section for more information
        |

    .. tab-container:: Supercomputer
        :title: Supercomputer

        |
        | Please, check the :ref:`Supercomputers` section.
        |

    .. tab-container:: Docker
        :title: Docker - PyCOMPSs Player

        |
        | **Requirements:**
        |
        | - Python 2/3 and pip 2/3
        | - Docker
        |
        | TODO: Add instructions to install pycompss-player.
        |


Write your first app
--------------------

Choose your flavour:

.. content-tabs::

    .. tab-container:: Java
        :title: Java

        .. rubric:: Java Increment

        Code

        .. rubric:: Execution

        Command

        .. rubric:: Output

        Output

        .. rubric:: Task dependency graph

        how to get and generated Graph


    .. tab-container:: Python
        :title: Python

        Let's write your first Python application parallelized with PyCOMPSs. |br|
        Consider the following code:

        .. code-block:: python
              :name: python-increment
              :caption: ``increment.py``

              import time
              from pycompss.api.api import compss_wait_on
              from pycompss.api.task import task

              @task(returns=1)
              def increment(value):
                time.sleep(value * 2)  # mimic some computational time
                return value + 1

              def main():
                  values = [1, 2, 3, 4]
                  start = time.time()
                  for pos in range(len(values)):
                      values[pos] = increment(values[pos])
                  values = compss_wait_on(values)
                  assert values == [2, 3, 4, 5]
                  print(values)
                  print("Elapsed time: " + str(time.time() - start_time))

              if __name__=='__main__':
                  main()

        This code increments the elements of an array (``values``) by calling
        iteratively to the ``increment`` function. |br|
        The increment function sleeps the number of seconds indicated by the
        ``value`` parameter to represent some computational time. |br|
        On a normal python execution, each element of the array will be
        incremented after the other (sequentially), accumulating the
        computational time. |br|
        PyCOMPSs is able to parallelize this loop thanks to its ``@task``
        decorator, and synchronize the results with the ``compss_wait_on``
        API call.

        *Copy and paste it into* ``increment.py``.

        .. rubric:: Execution

        Now let's execute ``increment.py``. To this end, we will use the
        ``runcompss`` script provided by COMPSs.

        .. code-block:: console

            $ runcompss -g increment.py
              [Output in next step]

        .. note::
            The ``-g`` flag enables the task dependency graph generation (*used later*).

            The ``runcompss`` command has a lot of supported options that can be checked with the ``-h`` flag.

        .. tip::
            It is possible to run also with the ``python`` command using the ``pycompss`` module,
            which accepts the same flags as ``runcompss``:

            .. code-block:: console

               $ python -m pycompss -g increment.py  # Parallel execution
                 [Output in next step]

            Having PyCOMPSs installed also enables to run the same code sequentially without the need of removing the PyCOMPSs syntax.

            .. code-block:: console

               $ python increment.py  # Sequential execution
                 [2, 3, 4, 5]
                 Elapsed time: 20.0161030293


        .. rubric:: Output

        .. code-block:: console

            $ runcompss -g increment.py
              [  INFO] Inferred PYTHON language
              [  INFO] Using default location for project file: /opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml
              [  INFO] Using default location for resources file: /opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml
              [  INFO] Using default execution type: compss

              ----------------- Executing increment.py --------------------------

              WARNING: COMPSs Properties file is null. Setting default values
              [(433)    API]  -  Starting COMPSs Runtime v2.6.rc2004 (build 20200422-1315.r5a8fb3e9c015da38836572fb943623231d54e868)
              [2, 3, 4, 5]
              Elapsed time: 11.5068922043
              [(4389)    API]  -  Execution Finished

              ------------------------------------------------------------

        **Nice!** we have the expected output... and PyCOMPSs has been able to
        run the same application in almost half of the time required by the
        sequential execution... *What happened under the hood?*

        COMPSs has started a master and one worker (by default configured to execute up to four tasks at the same time),
        executed the application, and offloaded the tasks execution to the worker.

        Let's check the task dependency graph to see the parallelism that
        COMPSs has extracted and taken advantage of.

        .. rubric:: Task dependency graph

        COMPSs stores the generated task dependecy graph within the
        ``$HOME/.COMPSs/<APP_NAME>_<00-99>/monitor`` directory in dot format. |br|
        The generated graph is ``complete_graph.dot`` file, which can be
        displayed with any dot viewer.

        .. tip::

            COMPSs provides the ``compss_gengraph`` script which converts the
            given dot file into pdf.

            .. code-block:: console

                $ cd $HOME/.COMPSs/increment.py_01/monitor
                $ compss_gengraph complete_graph.dot
                $ evince complete_graph.pdf  # or use any other pdf viewer you like

        And you should see:

        .. figure:: ./Figures/increment.png
           :name: increment_graph
           :alt: The dependency graph of the increment application
           :align: center
           :width: 30.0%

           The dependency graph of the increment application

        COMPSs has detected that the increment of each element is independent,
        and consequently, that all of them can be done in parallel. In this
        particular application, there are four ``increment`` tasks, and since
        the worker is able to run four tasks at the same time, all of them can
        be executed in parallel saving precious time.

        .. rubric:: Check the performance

        Let's run it again with the tracing flag enabled:

        .. code-block:: console

            $ runcompss -t increment.py
              [  INFO] Inferred PYTHON language
              [  INFO] Using default location for project file: /opt/COMPSs//Runtime/configuration/xml/projects/default_project.xml
              [  INFO] Using default location for resources file: /opt/COMPSs//Runtime/configuration/xml/resources/default_resources.xml
              [  INFO] Using default execution type: compss

              ----------------- Executing increment.py --------------------------

              Welcome to Extrae 3.5.3

              [... Extrae prolog ...]

              WARNING: COMPSs Properties file is null. Setting default values
              [(434)    API]  -  Starting COMPSs Runtime v2.6.rc2004 (build 20200422-1315.r5a8fb3e9c015da38836572fb943623231d54e868)
              [2, 3, 4, 5]
              Elapsed time: 13.1016821861

              [... Extrae eplilog ...]

              mpi2prv: Congratulations! ./trace/increment.py_compss_trace_1587562240.prv has been generated.
              [(24117)    API]  -  Execution Finished

              ------------------------------------------------------------

        The execution has finished successfully and the trace has been generated
        in the ``$HOME/.COMPSs/<APP_NAME>_<00-99>/trace`` directory in prv format,
        which can be displayed and analysed with `PARAVER <https://tools.bsc.es/paraver>`_.

        .. code-block:: console

            $ cd $HOME/.COMPSs/increment.py_02/trace
            $ wxparaver increment.py_compss_trace_*.prv

        Once Paraver has started, lets visualize the tasks:

        - Click in ``File`` and then in ``Load Configuration``

        - Look for ``/PATH/TO/COMPSs/Dependencies/paraver/cfgs/compss_tasks.cfg`` and click ``Open``

        And you should see:

        .. figure:: ./Figures/increment_trace.png
           :name: increment_trace
           :alt: Trace of the increment application
           :align: center
           :width: 50.0%

           Trace of the increment application

        The X axis represents the time, and the Y axis the deployed processes
        (the first three (1.1.1-1.1.3) belong to the master and the fourth belongs
        to the master process in the worker (1.2.1) whose events are
        shown with the ``compss_runtime.cfg`` configuration file).

        The rest, represent the worker cores, which process the ``increment`` tasks
        (shown in blue). We can quickly see that the four `increment` tasks
        have been executed in parallel.

        Paraver is a very powerful tool for performance analysis. For more information,
        check the :ref:`Tracing` Section.


    .. tab-container:: C
        :title: C/C++

        .. rubric:: C/C++ Increment

        Code

        .. rubric:: Execution

        Command

        .. rubric:: Output

        Output

        .. rubric:: Task dependency graph

        how to get and generated Graph


Useful information
------------------

Choose your flavour:

.. content-tabs::

    .. tab-container:: Java
        :title: Java

        - Syntax detailed information -> :ref:`Java`

        - Constraint definition -> :ref:`Constraints`

        - Execution details -> :ref:`Executing COMPSs applications`

        - Graph, tracing and monitoring facilities -> :ref:`COMPSs Tools`

        - Performance analysis -> :ref:`Tracing`

        - Troubleshooting -> :ref:`Common Issues`

        - Sample applications -> :ref:`Java Sample applications`

        - Using COMPSs with persistent storage frameworks (e.g. dataClay, Hecuba) -> :ref:`Storage Integration`

    .. tab-container:: Python
        :title: Python

        - Syntax detailed information -> :ref:`Python`

        - Constraint definition -> :ref:`Constraints`

        - Execution details -> :ref:`Executing COMPSs applications`

        - Graph, tracing and monitoring facilities -> :ref:`COMPSs Tools`

        - Performance analysis -> :ref:`Tracing`

        - Troubleshooting -> :ref:`Common Issues`

        - Sample applications -> :ref:`Python Sample applications`

        - Using COMPSs with persistent storage frameworks (e.g. dataClay, Hecuba) -> :ref:`Storage Integration`

    .. tab-container:: C
        :title: C/C++

        - Syntax detailed information -> :ref:`C/C++`

        - Constraint definition -> :ref:`Constraints`

        - Execution details -> :ref:`Executing COMPSs applications`

        - Graph, tracing and monitoring facilities -> :ref:`COMPSs Tools`

        - Performance analysis -> :ref:`Tracing`

        - Troubleshooting -> :ref:`Common Issues`

        - Sample applications -> :ref:`C/C++ Sample applications`

        - Using COMPSs with persistent storage frameworks (e.g. dataClay, Hecuba) -> :ref:`Storage Integration`
