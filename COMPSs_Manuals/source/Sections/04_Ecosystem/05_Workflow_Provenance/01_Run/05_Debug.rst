Time statistics, log and debug
==============================

When provenance generation is activated, and after the application has finished, the workflow provenance generation
script will be automatically triggered. A number of log messages related to provenance can bee seen, which return
interesting information regarding the provenance generation process. They can all be filtered by doing a ``grep`` in
the output log of the application using the ``PROVENANCE`` expression.

The most important message returned at the end is the total time provenance generation took, to understand if, compared to the
total execution time of the application, this time is ok.

.. code-block:: console

    PROVENANCE | Workflow Provenance generation TOTAL EXECUTION TIME: 8.130196809768677 s

However, other blocks provide also detailed information to assess if any part of the generation can be problematic:

.. code-block:: console

    PROVENANCE | Generating graph for Workflow Provenance
    PROVENANCE | Number of edges in the graph: 359
    Output file: /Users/user/.COMPSs/37021218//monitor/complete_graph.svg
    INFO: Generating Graph with legend
    DONE
    PROVENANCE | Ended generating graph for Workflow Provenance. TIME: 1 s


This first block indicates that the workflow diagram in SVG format is being generated. When this part finishes, the time
in seconds will be reported. As mentioned earlier, complex workflows can lead to large graph diagram generation times, and that
is why the number of edges in the graph is also reported.

.. WARNING::
    If the number of edges is larger than 6500, the graph diagram generation won't
    be triggered to avoid large generation times.

.. code-block:: console

    PROVENANCE | STARTING RO-CRATE GENERATION SCRIPT
    PROVENANCE | PROFILING | Profiling plots generation TIME: 3.15 s.
    PROVENANCE | COMPSs version: '3.4', main_entity: '/Users/user/Apps_COMPSs/CAELESTIS/ALYA-COMPLETE/Workflows/WORKFLOWS/api.py'
    PROVENANCE | COMPSs runtime detected inputs (12)
    PROVENANCE | COMPSs runtime detected outputs (4)
    PROVENANCE | dataprovenance.log processing TIME: 0.0025789737701416016 s

This second block shows the time it took to generate the profiling plots, and the COMPSs version and 
the ``mainEntity`` detected (i.e. the source file that contains the main method from the COMPSs
application). Besides, it reports how many input and output data assets have been detected automatically by the COMPSs
runtime, and the time it took to run the master information analysis (i.e. the dataprovenance.log processing time).

.. code-block:: console

    PROVENANCE | Application source files detected (18)
    PROVENANCE | RO-Crate adding source files TIME: 0.005171775817871094 s
    PROVENANCE | RO-Crate adding input files TIME (Persistence: True): 0.012867927551269531 s
    PROVENANCE | RO-Crate adding output files TIME (Persistence: True): 0.007106304168701172 s



The third block first details how many source files have been detected from the ``sources`` term defined
in the YAML configuration file. Then, it provides a set of times to understand if any overhead is caused by the
workflow provenance generation script. The first time is the time taken to add the files that are included
physically in the crate (this is, application source files, workflow diagram, ...). And the second and third are the times
spent by the script to add all input and output files, detailing if data persistence was established as ``True`` or ``False``.
If ``True``, the files are physically copied to the crate. If ``False``, only references to the location of the files are
included.

.. code-block:: console

    PROVENANCE | Added resource profiling information TIME: 0.010936975479125977 s
    PROVENANCE | RO-Crate adding CreateAction TIME: 0.013741016387939453 s
    PROVENANCE | RO-Crate Provenance Run Crate profile total TIME: 0.11636114120483398 s
    PROVENANCE | RO-Crate writing to disk TIME: 4.811898708343506 s
    PROVENANCE | Workflow Provenance generation TOTAL EXECUTION TIME: 8.130196809768677 s
    PROVENANCE | COMPSs Workflow Provenance successfully generated in ZIP file:
            CAELESTIS_MN5_4_NODES.zip
    PROVENANCE | ENDED WORKFLOW PROVENANCE SCRIPT

The fourth and final block states first how much time took to write profiling information in the metadata,
the time to store the main workflow run information (CreateAction) and the time to record details on every
single task of the run (Provenance Run Crate). Besides, 
the time taken to write the crate to disk and the total
execution time of the whole workflow provenance generation script are also reported, and the final message details the name of the
sub-folder or zip file where the RO-Crate package has been generated.

.. WARNING::
    When ``data_persistence`` is set to ``True`` and the application uses large datasets (hundreds of MBs), the time to write all this
    data to disk can grow quickly.

During the workflow provenance generation, some messages labeled as ``WARNING`` may appear. The situations reported
with warning messages are non-critical situations where some automatic decisions were taken by the generation script,
so the user should double check if the decision taken is correct. Some examples follow:

.. code-block:: console

    PROVENANCE | WARNING: A parent directory of a previously added sub-directory is being added. Some files will be traversed twice in: /Users/user/COMPSs-DP/matmul_files/in
    PROVENANCE | WARNING: A file addition was attempted twice: /Users/user/COMPSs-DP/matmul_files/in/A/A.0.0 in /Users/user/COMPSs-DP/matmul_files/in
    PROVENANCE | WARNING: 'Agent' not specified in TEST_DUPLICATED_SOURCES.yaml. First author selected by default.

.. TIP::
    In case of need for debugging the workflow provenance generation, an environment variable called ``COMPSS_PROV_DEBUG``
    has been defined to enable a larger amount of provenance generation output messages in order to detect any possible issues.
    Before the execution, users must define the variable using the command ``export COMPSS_PROV_DEBUG=True``.
