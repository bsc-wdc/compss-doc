--------------------
Recording activation
--------------------

The way of activating the recording of workflow provenance with COMPSs is very simple.
One must only enable the ``-p`` or ``--provenance`` flag when using ``runcompss``,
``enqueue_compss``, or ``pycompss run`` to run or submit a COMPSs application. It is important to highlight that the
``--provenance`` flag accepts a custom name for the YAML file with the application's details (see previous
Section :ref:`Sections/05_Tools/04_Workflow_Provenance/02_YAML:YAML configuration file`). This is
specified using the ``--provenance=my_yaml_file.yaml`` option, as shown in the ``runcompss`` help:

.. code-block:: console

    $ runcompss -h

    (...)
    --provenance=<yaml>,
    --provenance, -p    Generate COMPSs workflow provenance data in RO-Crate format using a YAML configuration file. Automatically activates --graph and --output_profile.
                        Default: ro-crate-info.yaml


.. WARNING::

    As stated in the help, provenance automatically activates both ``--graph`` and ``--output_profile`` options.
    Consider that the graph diagram generation can take some extra time at the end of the execution of your
    application, therefore, adjust the ``--exec_time`` accordingly.

In the case of extremely large workflows (e.g. a workflow
with tenths of thousands of task nodes, or tenths of thousands of files used as inputs or outputs), the extra time
needed to generate the workflow provenance with RO-Crate may be a problem in systems with strict run time constraints.
Besides, in the COMPSs specific case, workflows with a large number of edges can lead to large
workflow diagram generation time with ``compss_gengraph``.
In these cases, the workflow execution may end correctly, but the extra processing time needed to generate the
provenance may be larger than the specified execution time limit. This means that the process may be killed while
generating the provenance, therefore it won't be created correctly.

.. WARNING::
    As a failsafe, we automatically disable workflow diagram generation for workflows with more than 6500 edges.
    If you want to generate the diagram anyway, you can
    trigger the diagram generation manually with ``compss_gengraph`` or ``pycompss gengraph``.

For these extreme cases, our workflow provenance generation script can be triggered offline at any moment
after the workflow has executed correctly, thanks to our design. From the working directory of the application, the
following commands can be used:

.. code-block:: console

    $ $COMPSS_HOME/Runtime/scripts/utils/compss_gengraph svg $BASE_LOG_DIR/monitor/complete_graph.dot

    $ export PYTHONPATH=$COMPSS_HOME/Runtime/scripts/system/:$PYTHONPATH

    $ python3 $COMPSS_HOME/Runtime/scripts/system/provenance/generate_COMPSs_RO-Crate.py my_yaml_file.yaml $BASE_LOG_DIR/dataprovenance.log

In these commands, ``COMPSS_HOME`` is where your COMPSs installation is located, and ``BASE_LOG_DIR`` points to the path where the
application run logs are stored (see Section :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/01_Local/02_Results_and_logs:Logs`
for more details on where to locate these logs). ``compss_gengraph``
generates the workflow diagram to be added to the crate, but if its generation time is a concern, or the user does not
want it to be included in the crate, the command can be skipped. The second command runs the
``generate_COMPSs_RO-Crate.py`` Python script, that uses the information provided by the user
in the ``my_yaml_file.yaml`` file (or ``ro-crate-info.yaml`` by default)
combined with the file accesses information registered by the COMPSs runtime in the ``dataprovenance.log`` file. The
result is a sub-directory ``COMPSs_RO-Crate_[timestamp]/`` that contains the workflow provenance of the run (see next sub-section
for a detailed description of its content).

.. TIP::
    The workflow provenance generation script will produce in the standard output the precise commands to be used for the
    particular case of the application in use. An example on how the message would be printed follows:

    .. code-block:: console

        PROVENANCE | STARTING WORKFLOW PROVENANCE SCRIPT
        PROVENANCE | If needed, Provenance generation can be triggered by hand using the following commands:
            /apps/GPP/COMPSs/3.3.3/Runtime/scripts/utils/compss_gengraph svg /home/bsc/bsc019057/.COMPSs/4471214//monitor/complete_graph.dot
            export PYTHONPATH=/apps/GPP/COMPSs/3.3.3/Runtime/scripts/system/:$PYTHONPATH
            python3 -O /apps/GPP/COMPSs/3.3.3/Runtime/scripts/system/provenance/generate_COMPSs_RO-Crate.py FULL_SINGULARITY.yaml /home/bsc/bsc019057/.COMPSs/4471214//dataprovenance.log
        PROVENANCE | TIP for BSC cluster users: before triggering generation by hand, run first: salloc -p interactive
        ...

