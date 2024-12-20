------------------------------
Time statistics, log and debug
------------------------------

When provenance generation is activated, and after the application has finished, the workflow provenance generation
script will be automatically triggered. A number of log messages related to provenance can bee seen, which return
interesting information regarding the provenance generation process. They can all be filtered by doing a ``grep`` in
the output log of the application using the ``PROVENANCE`` expression.

.. code-block:: console

    PROVENANCE | Generating graph for Workflow Provenance
    PROVENANCE | Number of edges in the graph:        8
    Output file: /Users/rsirvent/.COMPSs/matmul_files.py_01//monitor/complete_graph.svg
    INFO: Generating Graph with legend
    DONE
    PROVENANCE | Ended generating graph for Workflow Provenance. TIME: 1 s

This first block indicates that the workflow diagram in SVG format is being generated. When this part finishes, the time
in seconds will be reported. As mentioned earlier, complex workflows can lead to large graph diagram generation times, and that
is why the number of edges in the graph is also reported. If the number is larger than 6500, the graph diagram generation won't
be triggered to avoid large generation times.

.. code-block:: console

    PROVENANCE | STARTING RO-CRATE GENERATION SCRIPT
    PROVENANCE | COMPSs version: 3.3.rc2402, out_profile: App_Profile.json, main_entity: /Users/rsirvent/COMPSs-DP/matmul_files/matmul_files.py
    PROVENANCE | COMPSs runtime detected inputs (12)
    PROVENANCE | COMPSs runtime detected outputs (4)
    PROVENANCE | dataprovenance.log processing TIME: 0.0001647472381591797 s


This second block shows the COMPSs version detected, the name of the file containing the execution profile of the
application, and the ``mainEntity`` detected (i.e. the source file that contains the main method from the COMPSs
application). Besides, it reports how many input and output data assets have been detected automatically by the COMPSs
runtime, and the time it took to run its analysis (i.e. the dataprovenance.log processing time).

.. code-block:: console

    PROVENANCE | Application source files detected (11)
    PROVENANCE | RO-Crate adding source files TIME: 0.055359840393066406 s
    PROVENANCE | RO-Crate adding input files TIME (Persistence: True): 0.0027692317962646484 s
    PROVENANCE | RO-Crate adding output files TIME (Persistence: True): 0.0006499290466308594 s


The third block first details how many source files have been detected from the ``sources`` term defined
in the ``ro-crate-info.yaml`` file. Then, it provides a set of times to understand if any overhead is caused by the
workflow provenance generation script. The first time is the time taken to add the files that are included
physically in the crate (this is, application source files, workflow diagram, ...). And the second and third are the times
spent by the script to add all input and output files, detailing if data persistence was established as ``True`` or ``False``.
If ``True``, the files are physically copied to the crate. If ``False``, only references to the location of the files are
included.

.. code-block:: console

    PROVENANCE | RO-Crate writing to disk TIME: 0.02508401870727539 s
    PROVENANCE | Workflow Provenance generation TOTAL EXECUTION TIME: 0.10874414443969727 s
    PROVENANCE | COMPSs Workflow Provenance successfully generated in sub-folder:
        COMPSs_RO-Crate_db892d40-7929-461e-b06a-1b2120008f4f/
    PROVENANCE | ENDED WORKFLOW PROVENANCE SCRIPT

The fourth and final block states the time taken to record the ``ro-crate-metadata.json`` file to disk, the total
execution time of the whole workflow provenance generation script, and the final message details the name of the
sub-folder where the RO-Crate package has been generated.

During the workflow provenance generation, some messages labeled as ``WARNING`` may appear. The situations reported
with warning messages are non-critical situations where some automatic decisions were taken by the generation script,
so the user should double check if the decision taken is correct. Some examples follow:

.. code-block:: console

    PROVENANCE | WARNING: A parent directory of a previously added sub-directory is being added. Some files will be traversed twice in: /Users/rsirvent/COMPSs-DP/matmul_files/in
    PROVENANCE | WARNING: A file addition was attempted twice: /Users/rsirvent/COMPSs-DP/matmul_files/in/A/A.0.0 in /Users/rsirvent/COMPSs-DP/matmul_files/in
    PROVENANCE | WARNING: 'Agent' not specified in TEST_DUPLICATED_SOURCES.yaml. First author selected by default.

.. TIP::
    In case of need for debugging the workflow provenance generation, an environment variable called ``COMPSS_PROV_DEBUG``
    has been defined to enable a larger amount of provenance generation output messages in order to detect any possible issues.
    Before the execution, users must define the variable using the command ``export COMPSS_PROV_DEBUG=True``.

