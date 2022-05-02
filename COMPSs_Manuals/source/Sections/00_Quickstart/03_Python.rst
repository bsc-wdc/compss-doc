.. |qpybr| raw:: html

   <br />


Let's write your first Python application parallelized with PyCOMPSs. |qpybr|
Consider the following code:

.. code-block:: python
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
          start_time = time.time()
          for pos in range(len(values)):
              values[pos] = increment(values[pos])
          values = compss_wait_on(values)
          assert values == [2, 3, 4, 5]
          print(values)
          print("Elapsed time: " + str(time.time() - start_time))

      if __name__=='__main__':
          main()

This code increments the elements of an array (``values``) by calling
iteratively to the ``increment`` function. |qpybr|
The increment function sleeps the number of seconds indicated by the
``value`` parameter to represent some computational time. |qpybr|
On a normal python execution, each element of the array will be
incremented after the other (sequentially), accumulating the
computational time. |qpybr|
PyCOMPSs is able to parallelize this loop thanks to its ``@task``
decorator, and synchronize the results with the ``compss_wait_on``
API call.

.. NOTE::

    If you are using the PyCOMPSs CLI (`pycompss-cli <https://pypi.org/project/pycompss-cli/>`_),
    it is time to deploy the COMPSs environment within your current folder:

    .. code-block:: console

            $ pycompss init

    Please, be aware that the first time needs to download the docker image from the
    repository, and it may take a while.

*Copy and paste the increment code it into* ``increment.py``.

.. rubric:: Execution

Now let's execute ``increment.py``. To this end, we will use the
``runcompss`` script provided by COMPSs:

.. code-block:: console

    $ runcompss -g increment.py
      [Output in next step]

Or alternatively, the ``pycompss run`` command if using the PyCOMPSs CLI
(which wraps the ``runcompss`` command and launches it within the COMPSs' docker
container):

.. code-block:: console

    $ pycompss run -g increment.py
      [Output in next step]

.. note::
    The ``-g`` flag enables the task dependency graph generation (*used later*).

    The ``runcompss`` command has a lot of supported options that can be checked with the ``-h`` flag.
    They can also be used within the ``pycompss run`` command.

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
      [(433)    API]  -  Starting COMPSs Runtime v2.7 (build 20200519-1005.r6093e5ac94d67250e097a6fad9d3ec00d676fe6c)
      [2, 3, 4, 5]
      Elapsed time: 11.5068922043
      [(4389)    API]  -  Execution Finished

      ------------------------------------------------------------

**Nice!** it run successfully in my 8 core laptop, we have the expected output,
and PyCOMPSs has been able to run the ``increment.py`` application in almost half
of the time required by the sequential execution. *What happened under the hood?*

COMPSs started a master and one worker (by default configured to execute up to four tasks at the same time)
and executed the application (offloading the tasks execution to the worker).

Let's check the task dependency graph to see the parallelism that
COMPSs has extracted and taken advantage of.

.. rubric:: Task dependency graph

COMPSs stores the generated task dependecy graph within the
``$HOME/.COMPSs/<APP_NAME>_<00-99>/monitor`` directory in dot format. |qpybr|
The generated graph is ``complete_graph.dot`` file, which can be
displayed with any dot viewer.

.. tip::

    COMPSs provides the ``compss_gengraph`` script which converts the
    given dot file into pdf.

    .. code-block:: console

        $ cd $HOME/.COMPSs/increment.py_01/monitor
        $ compss_gengraph complete_graph.dot
        $ evince complete_graph.pdf  # or use any other pdf viewer you like

    It is also available within the PyCOMPSs CLI:

    .. code-block:: console

        $ cd $HOME/.COMPSs/increment.py_01/monitor
        $ pycompss gengraph complete_graph.dot
        $ evince complete_graph.pdf  # or use any other pdf viewer you like

And you should see:

  .. figure:: /Sections/00_Quickstart/Figures/increment.png
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
      [(434)    API]  -  Starting COMPSs Runtime v2.7 (build 20200519-1005.r6093e5ac94d67250e097a6fad9d3ec00d676fe6c)
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

.. NOTE::

    In the case of using the PyCOMPSs CLI, the trace will be generated
    in the ``.COMPSs/<APP_NAME>_<00-99>/trace`` directory:

    .. code-block:: console

        $ cd .COMPSs/increment.py_02/trace
        $ wxparaver increment.py_compss_trace_*.prv

Once Paraver has started, lets visualize the tasks:

- Click in ``File`` and then in ``Load Configuration``

- Look for ``/PATH/TO/COMPSs/Dependencies/paraver/cfgs/compss_tasks.cfg`` and click ``Open``.

.. NOTE::

    In the case of using the PyCOMPSs CLI, the configuration files can be
    obtained by downloading them from the `COMPSs repositoy <https://github.com/bsc-wdc/compss/tree/stable/files/paraver/cfgs>`_.

And you should see:

  .. figure:: /Sections/00_Quickstart/Figures/increment_trace.png
      :alt: Trace of the increment application
      :align: center
      :width: 50.0%

      Trace of the increment application

The X axis represents the time, and the Y axis the deployed processes
(the first three (1.1.1-1.1.3) belong to the master and the fourth belongs
to the master process in the worker (1.2.1) whose events are
shown with the ``compss_runtime.cfg`` configuration file).

The ``increment`` tasks are depicted in blue.
We can quickly see that the four `increment` tasks have been executed in parallel
(one per core), and that their lengths are different (depending on the
computing time of the task represented by the ``time.sleep(value * 2)`` line).

Paraver is a very powerful tool for performance analysis. For more information,
check the :ref:`Sections/05_Tools/03_Tracing:Tracing` Section.

.. NOTE::

    If you are using the PyCOMPSs CLI, it is time to stop the COMPSs environment:

    .. code-block:: console

            $ pycompss stop
