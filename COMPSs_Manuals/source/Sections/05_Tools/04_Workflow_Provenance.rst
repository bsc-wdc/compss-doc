Workflow Provenance
===================

In order to achieve **Reproducibility** and **Replicability** with your experiments
using COMPSs, the runtime includes the capacity of recording details of the
application's execution, also known as *Workflow Provenance*. This is supported for both Python
and Java COMPSs applications. More technical details on how Provenance is generated in COMPSs using a lightweight approach
that does not introduce overhead to the workflow execution can be found in the paper:

- `Automatic, Efficient and Scalable Provenance Registration for FAIR HPC Workflows <http://dx.doi.org/10.1109/WORKS56498.2022.00006>`_

Moreover, a set of slides is available `here <https://zenodo.org/record/7701868>`_.

When the provenance option is activated, the runtime records every access
to a file or directory specified in the application, as well as its direction (IN,
OUT, INOUT). In addition to this, other information such as the parameters passed as inputs in the command line
that submitted the application, its source files, workflow image and task profiling statistics, authors and
their institutions, ... are also stored.
All this information is later used to record the Workflow Provenance
of your application using the `RO-Crate specification <https://www.researchobject.org/ro-crate/1.1/>`_, and with the assistance of
the `ro-crate-py library <https://github.com/ResearchObject/ro-crate-py>`_. RO-Crate is based on
JSON-LD (JavaScript Object Notation for Linked Data), is
much simpler than other standards and tools created to record Provenance, and
that is why it has been adopted in a number of `communities <https://www.researchobject.org/ro-crate/in-use/>`_. Using RO-Crate
to register the execution's information ensures
not only to register correctly the Provenance of a COMPSs application run, but
also compatibility with some existing portals that already embrace
RO-Crate as their core format for representing metadata, such as `WorkflowHub <https://workflowhub.eu/>`_. Our RO-Crate
format is compliant with the `Workflow RO-Crate Profile v1.0 <https://w3id.org/workflowhub/workflow-ro-crate/1.0>`_ and the
`Workflow Run Crate Profile v0.1 <https://w3id.org/ro/wfrun/workflow/0.1>`_.


Software dependencies
---------------------

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

Our implementation has been tested with ``ro-crate-py`` version ``0.7.0`` and earlier.


Previous needed information
---------------------------

There are certain pieces of information which must be included when registering the provenance of a workflow that
the COMPSs runtime cannot automatically infer, such as the authors of an application. For specifying all these
fields that are needed to generate an RO-Crate but cannot be automatically obtained, we have created a simple YAML
structure where the user can specify them. They need to provide in their working directory (i.e. where the application
is going to be run) a YAML file named ``ro-crate-info.yaml`` that follows the next template structure:

.. code-block:: yaml

    COMPSs Workflow Information:
      name: Name of your COMPSs application
      description: Detailed description of your COMPSs application
      license: Apache-2.0
        # URL preferred, but these strings are accepted: https://about.workflowhub.eu/Workflow-RO-Crate/#supported-licenses
      sources_dir: [path_to/dir_1, path_to/dir_2]
        # Optional: List of directories containing the application source files. Relative or absolute paths can be used
      sources_main_file: my_main_file.py
        # Optional: Name of the main file of the application, located in one of the sources_dir.
        # Relative paths from a sources_dir entry, or absolute paths can be used
      files: [main_file.py, aux_file_1.py, aux_file_2.py]
        # List of application files. Relative or absolute paths can be used

    Authors:
      - name: Author_1 Name
        e-mail: author_1@email.com
        orcid: https://orcid.org/XXXX-XXXX-XXXX-XXXX
        organisation_name: Institution_1 name
        ror: https://ror.org/XXXXXXXXX
          # Find them in ror.org
      - name: Author_2 Name
        e-mail: author2@email.com
        orcid: https://orcid.org/YYYY-YYYY-YYYY-YYYY
        organisation_name: Institution_2 name
        ror: https://ror.org/YYYYYYYYY
          # Find them in ror.org

    Submitter:
      name: Name
      e-mail: submitter@email.com
      orcid: https://orcid.org/XXXX-XXXX-XXXX-XXXX
      organisation_name: Submitter Institution name
      ror: https://ror.org/XXXXXXXXX
        # Find them in ror.org

.. WARNING::

    If no YAML file is provided, the runtime will fail to generate provenance, and will automatically generate an
    ``ro-crate-info_TEMPLATE.yaml`` file that the user can edit to add their details.

As you can see, there are three main blocks in the YAML:

- **COMPSs Workflow Information:** Where details on the application are provided.

- **Authors:** Where authors' details are given.

- **Submitter:** The person running the workflow in the computing resources.

More specifically, in the **COMPSs Workflow Information** section:

- The ``name`` and ``description`` fields are free text, where a long name and description of
  the application must be provided.

- The ``license`` field is preferred to be specified by providing an URL to the license, but a set of
  predefined strings are also supported, and can be found here:
  https://about.workflowhub.eu/Workflow-RO-Crate/#supported-licenses

- ``sources_dir`` can be a single path, or a list of paths where application source files can be found. Our script
  will add ALL files (i.e. not only source files, but any file found) and sub-directories inside each of the paths
  specified. The sub-directories structure is respected
  when the files are added in the crate (inside a sub-directory ``application_sources``).

- ``sources_main_file`` is the name of the main source file of the application, and may be specified if the user wants to select
  a particular file as such. The COMPSs runtime detects automatically the main source of an application, therefore this is a way
  to override the detected file. The file can be specified with a relative path inside one of the
  directories listed in ``sources_dir``. An absolute path can also be used.

- ``files`` is a single file or a list of all the source files of the application (typically all ``.py`` files for Python
  applications, or ``.java``, ``.class``, ``.jar`` files for Java ones). Both relative and absolute paths can be used.
  All files specified here will be added in the root of the sub-directory ``application_sources`` from the resulting
  crate. If the script is unable to automatically
  identify the main source file of the application, the first file of this list may be considered as such.

The ``sources_dir`` and ``files`` terms are complementary to each other. An ``ro-crate-info.yaml`` could use the term
``files`` alone or ``sources_dir`` alone, but also both, if the user is willing to add a number of sub-directories
with source files, but also several files by hand.

.. WARNING::

    The term ``sources_main_file`` can only be used when ``sources_dir`` is defined. While the runtime is able to detect
    automatically the main file from application execution, this would enable to modify that automatic selection in case
    of need.

In the **Authors** section:

- ``name``, ``e-mail`` and ``organisation_name`` are strings corresponding to the author's name, e-mail and their
  institution. They are free text, but the ``e-mail`` field must follow the ``user@domain.top`` format.

- ``orcid`` refers to the ORCID identifier of the author. The IDs can be found and created at https://orcid.org/

- ``ror`` refers to the Research Organization Registry (ROR) identifier for an institution.
  They can be found at http://ror.org/

.. TIP::

    It is very important that the list of source files (defined with ``sources_dir`` or ``files``), ``orcid`` and
    ``ror`` terms are correctly defined, since the
    runtime will only register information for the list of source files defined, and the ``orcid`` and ``ror`` are
    used as unique identifiers in the RO-Crate specification.

The **Submitter** section has the same terms as the Authors section, but it specifically provides the details of the
person running the workflow, that can be different from the Authors.

.. WARNING::

    If no Submitter section is provided, the first Author will be considered by default as the submitter of the
    workflow.

In the following lines, we provide a YAML example for an out-of-core Matrix Multiplication PyCOMPSs application,
distributed with license Apache v2.0, with 2 source files, and authored by 3 persons from two different
institutions. Since no ``submitter`` is defined, the first author is considered as such by default.

.. code-block:: yaml

    COMPSs Workflow Information:
      name: COMPSs Matrix Multiplication, out-of-core using files
      description: Hypermatrix size 2x2 blocks, block size 2x2 elements
      license: Apache-2.0 #Provide better a URL, but these strings are accepted:
                        # https://about.workflowhub.eu/Workflow-RO-Crate/#supported-licenses
      files: [matmul_directory.py, matmul_tasks.py]

    Authors:
      - name: Raül Sirvent
        e-mail: Raul.Sirvent@bsc.es
        orcid: https://orcid.org/0000-0003-0606-2512
        organisation_name: Barcelona Supercomputing Center
        ror: https://ror.org/05sd8tv96
      - name: Rosa M. Badia
        e-mail: Rosa.M.Badia@bsc.es
        orcid: https://orcid.org/0000-0003-2941-5499
        organisation_name: Barcelona Supercomputing Center
        ror: https://ror.org/05sd8tv96
      - name: Adam Hospital
        e-mail: adam.hospital@irbbarcelona.org
        orcid: https://orcid.org/0000-0002-8291-8071
        organisation_name: IRB Barcelona
        ror: https://ror.org/01z1gye03

Also, another example of a COMPSs Java K-means application, where the usage of the ``sources_dir`` term can be seen.
We add to the crate the sub-directories that contain the ``.jar`` and ``.java`` files correspondingly. In this case,
a ``submitter`` is provided which is different from the person that wrote the application.

.. code-block:: yaml

    COMPSs Workflow Information:
      name: COMPSs K-means
      description: K-means clustering is a method of cluster analysis that aims to partition ''n'' points into ''k''
        clusters in which each point belongs to the cluster with the nearest mean. It follows an iterative refinement
        strategy to find the centers of natural clusters in the data.
      license: https://opensource.org/licenses/Apache-2.0 #Provide better a URL, but these strings are accepted:
                        # https://about.workflowhub.eu/Workflow-RO-Crate/#supported-licenses
      sources_dir: [jar/, src/]

    Authors:
      - name: Raül Sirvent
        e-mail: Raul.Sirvent@bsc.es
        orcid: https://orcid.org/0000-0003-0606-2512
        organisation_name: Barcelona Supercomputing Center
        ror: https://ror.org/05sd8tv96

    Submitter:
        - name: Adam Hospital
        e-mail: adam.hospital@irbbarcelona.org
        orcid: https://orcid.org/0000-0002-8291-8071
        organisation_name: IRB Barcelona
        ror: https://ror.org/01z1gye03

Usage
-----

The way of activating the recording of Workflow Provenance with COMPSs is very simple.
One must only enable the ``-p`` or ``--provenance`` flag when using ``runcomps`` or
``enqueue_compss`` to run or submit a COMPSs application, respectively.
As shown in the help option:
 
.. code-block:: console

    $ runcompss -h

    (...)
    --provenance, -p    Generate COMPSs workflow provenance data in RO-Crate format from YAML file. Automatically
                        activates -graph and -output_profile.
                        Default: false

.. WARNING::

    As stated in the help, provenance automatically activates both ``--graph`` and ``--output_profile`` options.
    Consider that the graph image generation can take some extra seconds at the end of the execution of your
    application, therefore, adjust the ``--exec_time`` accordingly.

In the case of extremely large workflows (e.g. a workflow
with tenths of thousands of task nodes, or tenths of thousands of files used as inputs or outputs), the extra time
needed to generate the workflow provenance with RO-Crate may be a problem in systems with strict run time constraints.
In these cases, the workflow execution may end correctly, but the extra processing to generate the provenance may be killed
by the system if it exceeds a certain limit, and the provenance will not be created correctly.

For this or any other similar situation, our workflow provenance generation script can be triggered offline at any moment
after the workflow has executed correctly, thanks to our design. From the working directory of the application, the
following commands may be used:

.. code-block:: console

    $ $COMPSS_HOME/Runtime/scripts/utils/compss_gengraph svg $BASE_LOG_DIR/monitor/complete_graph.dot

    $ python $COMPSS_HOME/Runtime/scripts/system/provenance/generate_COMPSs_RO-Crate.py ro-crate-info.yaml $BASE_LOG_DIR/dataprovenance.log

In these commands, ``COMPSS_HOME`` is where your COMPSs installation is located, and ``BASE_LOG_DIR`` points to the path where the
application run logs are stored (see Section :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/01_Local/02_Results_and_logs:Logs`
for more details on where to locate these logs). ``compss_gengraph``
generates the workflow image to be added to the crate, but if its generation time is a concern, or the user does not
want it to be included in the crate, the command can be skipped. The second command runs the
``generate_COMPSs_RO-Crate.py`` Python script, that uses the information provided by the user in ``ro-crate-info.yaml``
combined with the file accesses information registered by the COMPSs runtime in the ``dataprovenance.log`` file. The
result is a sub-directory ``COMPSs_RO-Crate_[uuid]/`` that contains the workflow provenance of the run (see next sub-section
for a detailed description).

Result
------

Once the application has finished, a new sub-folder under the application's Working Directory
will be created with the name ``COMPSs_RO-Crate_[uuid]/``, which is also known as *crate*. The contents of the
folder include all the elements needed to reproduce a COMPSs execution, and
are:

- **Application Source Files:** As detailed by the user in the ``ro-crate-info.yaml`` file,
  with the terms ``sources_dir`` and/or ``files``. They have to include
  the main source file and all auxiliary files that the application needs (e.g. ``.py``, ``.java``, ``.class``
  or ``.jar``). Optionally, the term ``sources_main_file`` can be used to manually select the main source file of
  the application. All application files are added to a sub-folder in the crate named ``application_sources``, where
  the ``sources_dir`` locations are included with their same folder tree structure. The files included with the
  ``files`` term are added to the root of the ``application_sources`` sub-folder in the crate.

- **complete_graph.svg:** The image of the workflow generated by the COMPSs runtime,
  as generated with the ``runcompss -g`` or ``--graph`` option.

- **App_Profile.json:** A set of task statistics of the application run recorded by the
  COMPSs runtime, as if the ``runcompss --output_profile=<path>`` option was enabled.
  It includes, for each resource and method executed: number of executions of the
  specific method, as well as maximum, average and minimum run time for the tasks.
  The name of the file can be customized using the ``--output_profile=<path>`` option.

- **compss_command_line_arguments.txt:** Stores the options passed by the command
  line when the application was submitted. This is very important for reproducing a COMPSs
  application, since input parameters could even potentially change the resulting workflow generated
  by the COMPSs runtime.

- **ro-crate-metadata.json:** The RO-Crate JSON main file describing the contents of
  this directory (crate) in the RO-Crate specification format. You can find examples in the following Sections.

.. WARNING::

    All previous file names (``complete_graph.svg``, ``App_Profile.json`` and ``compss_command_line_arguments.txt``)
    are automatically used to generate new files when using the ``-p`` or ``--provenance`` option.
    Avoid using these file names among
    your own files to avoid unwanted overwritings. You can change the resulting ``App_Profile.json`` name by using
    the ``--output_profile=/path_to/file`` flag.


Log and time statistics
-----------------------

When the provenance generation is activated, and after the application has finished, the workflow provenance generation
script will be automatically triggered. A number of log messages related to provenance can bee seen, which return
interesting information regarding the provenance generation process. They can all be filtered by doing a ``grep`` in
the output log of the application using the ``PROVENANCE`` expression.

.. code-block:: console

    PROVENANCE | GENERATING GRAPH FOR DATA PROVENANCE
    Output file: /Users/rsirvent/.COMPSs/matmul_directory.py_07//monitor/complete_graph.svg
    INFO: Generating Graph with legend
    DONE
    PROVENANCE | ENDED GENERATING GRAPH FOR DATA PROVENANCE. TIME: 1 s

This first block indicates that the workflow image in SVG format is being generated. When this part finishes, the time
in seconds will be reported. As mentioned earlier, complex workflows can lead to large graph generation times.

.. code-block:: console

    PROVENANCE | RUNNING DATA PROVENANCE SCRIPT
    PROVENANCE | Number of source files detected: 2
    PROVENANCE | COMPSs version: 3.1.rc2305, main_entity is: /Users/rsirvent/COMPSs-DP/matmul_directory/matmul_directory.py, out_profile is: App_Profile.json

This second block details how many source files have been detected from the ``sources_dir`` and ``files`` terms defined
in the ``ro-crate-py.yaml`` file. It also shows the COMPSs version detected, the ``mainEntity`` detected (i.e. the
source file that contains the main method from the COMPSs application), and the name of the file containing the
execution profile of the application.

.. code-block:: console

    PROVENANCE | RO-CRATE data_provenance.log processing TIME (process_accessed_files): 0.00011706352233886719 s
    PROVENANCE | RO-CRATE adding physical files TIME (add_file_to_crate): 0.001096963882446289 s
    PROVENANCE | RO-CRATE adding input files' references TIME (add_file_not_in_crate): 0.001238107681274414 s
    PROVENANCE | RO-CRATE adding output files' references TIME (add_file_not_in_crate): 0.00026798248291015625 s

The third block provides a set of times to understand if any overhead is caused by the script. The first time is the
time taken to process the data_provenance.log. The second is the time taken to add the files that are included
physically in the crate (this is, source files, workflow image, ...). And the third and the fourth are the times
spent by the script to add all input and output files of the workflow as references in the RO-Crate, respectively.

.. code-block:: console

    PROVENANCE | COMPSs RO-Crate created successfully in subfolder COMPSs_RO-Crate_aaf0cb82-a500-4c28-bbc8-439c37c2e210/
    PROVENANCE | RO-CRATE dump TIME: 0.004969120025634766 s
    PROVENANCE | RO-CRATE GENERATION TOTAL EXECUTION TIME: 0.014089107513427734 s
    PROVENANCE | ENDED DATA PROVENANCE SCRIPT

The fourth and final block details the name of the sub-folder where the RO-Crate has been generated, while stating
the time to record the ``ro-crate-metadata.json`` file to disk, and the total time execution of the whole script.

ro-crate-metadata.json PyCOMPSs example (Laptop)
------------------------------------------------

In the RO-Crate specification, the root file containing the metadata referring to the crate created is named
``ro-crate-metadata.json``. In these lines, we provide an example of an ro-crate-metadata.json file resulting from
a PyCOMPSs application execution in a laptop, specifically an out-of-core matrix multiplication example that includes matrices
``A`` and ``B`` as inputs in an ``inputs/`` sub-directory, and matrix ``C`` as the result of their multiplication
(which in the code is also passed as input, to have a matrix initialized with 0s).
For all the specific details on the fields provided in the JSON file, please refer to the
`RO-Crate specification Website <https://www.researchobject.org/ro-crate/1.1/>`_. Intuitively, if you search through
the JSON file you can find several interesting terms:

- **creator:** List of authors, identified by their ORCID.

- **publisher:** Organisations of the authors.

- **hasPart in ./:** lists all the files and directories this workflow needs and generates, and also the ones
  included in the crate. The URIs point to the hostname where the application has been run, thus, tells
  the user where the inputs and outputs can be found (in this example, a BSC laptop).

- **ComputationalWorkflow:** Main file of the application (in the example, ``application_sources/matmul_directory.py``).
  Includes a reference to the generated workflow image in the ``image`` field.

- **version:** The COMPSs specific version and build used to run this application. In the example: ``3.1.rc2305``.
  This is a very important field to achieve reproducibility or replicability, since COMPSs features may vary their
  behaviour in different versions of the programming model runtime.

- **CreateAction:** With the compliance to the Workflow Run Crate Profile v0.1, the details on the specific execution
  of the workflow are included in the ``CreateAction`` term.

  - The defined ``submitter`` is recorded as the ``agent``.

  - The ``description`` term records details on the host that run the workflow (architecture, Operating System version and COMPSs paths defined).

  - The ``object`` term makes reference to the input files used by the workflow.

  - The ``result`` term references the output files generated by the workflow.

We encourage the reader to navigate through this ``ro-crate-metadata.json`` file example to get familiar with its
contents. Many of the fields are easily and directly understandable.

.. code-block:: json

    {
        "@context": "https://w3id.org/ro/crate/1.1/context",
        "@graph": [
            {
                "@id": "./",
                "@type": "Dataset",
                "conformsTo": [
                    {
                        "@id": "https://w3id.org/ro/wfrun/process/0.1"
                    },
                    {
                        "@id": "https://w3id.org/ro/wfrun/workflow/0.1"
                    },
                    {
                        "@id": "https://w3id.org/workflowhub/workflow-ro-crate/1.0"
                    }
                ],
                "creator": [
                    {
                        "@id": "https://orcid.org/0000-0002-8291-8071"
                    },
                    {
                        "@id": "https://orcid.org/0000-0003-2941-5499"
                    },
                    {
                        "@id": "https://orcid.org/0000-0003-0606-2512"
                    }
                ],
                "datePublished": "2023-05-16T14:29:25+00:00",
                "description": "Hypermatrix size 2x2 blocks, block size 2x2 elements",
                "hasPart": [
                    {
                        "@id": "application_sources/matmul_directory.py"
                    },
                    {
                        "@id": "complete_graph.svg"
                    },
                    {
                        "@id": "App_Profile.json"
                    },
                    {
                        "@id": "compss_command_line_arguments.txt"
                    },
                    {
                        "@id": "application_sources/matmul_tasks.py"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.0.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.0.1"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.1.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.1.1"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.0.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.0.1"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.1.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.1.1"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.0.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.0.1"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.1.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.1.1"
                    }
                ],
                "license": "Apache-2.0",
                "mainEntity": {
                    "@id": "application_sources/matmul_directory.py"
                },
                "mentions": {
                    "@id": "#COMPSs_Workflow_Run_Crate_bsccs742.int.bsc.es_aff79a2b-6487-4932-9e9b-eed5f31b2666"
                },
                "name": "COMPSs Matrix Multiplication, out-of-core using files",
                "publisher": [
                    {
                        "@id": "https://ror.org/05sd8tv96"
                    },
                    {
                        "@id": "https://ror.org/01z1gye03"
                    }
                ]
            },
            {
                "@id": "ro-crate-metadata.json",
                "@type": "CreativeWork",
                "about": {
                    "@id": "./"
                },
                "conformsTo": [
                    {
                        "@id": "https://w3id.org/ro/crate/1.1"
                    },
                    {
                        "@id": "https://w3id.org/workflowhub/workflow-ro-crate/1.0"
                    }
                ]
            },
            {
                "@id": "https://orcid.org/0000-0003-0606-2512",
                "@type": "Person",
                "affiliation": {
                    "@id": "https://ror.org/05sd8tv96"
                },
                "contactPoint": {
                    "@id": "mailto:Raul.Sirvent@bsc.es"
                },
                "name": "Ra\u00fcl Sirvent"
            },
            {
                "@id": "mailto:Raul.Sirvent@bsc.es",
                "@type": "ContactPoint",
                "contactType": "Author",
                "email": "Raul.Sirvent@bsc.es",
                "identifier": "Raul.Sirvent@bsc.es",
                "url": "https://orcid.org/0000-0003-0606-2512"
            },
            {
                "@id": "https://ror.org/05sd8tv96",
                "@type": "Organization",
                "name": "Barcelona Supercomputing Center"
            },
            {
                "@id": "https://orcid.org/0000-0003-2941-5499",
                "@type": "Person",
                "affiliation": {
                    "@id": "https://ror.org/05sd8tv96"
                },
                "contactPoint": {
                    "@id": "mailto:Rosa.M.Badia@bsc.es"
                },
                "name": "Rosa M. Badia"
            },
            {
                "@id": "mailto:Rosa.M.Badia@bsc.es",
                "@type": "ContactPoint",
                "contactType": "Author",
                "email": "Rosa.M.Badia@bsc.es",
                "identifier": "Rosa.M.Badia@bsc.es",
                "url": "https://orcid.org/0000-0003-2941-5499"
            },
            {
                "@id": "https://orcid.org/0000-0002-8291-8071",
                "@type": "Person",
                "affiliation": {
                    "@id": "https://ror.org/01z1gye03"
                },
                "contactPoint": {
                    "@id": "mailto:adam.hospital@irbbarcelona.org"
                },
                "name": "Adam Hospital"
            },
            {
                "@id": "mailto:adam.hospital@irbbarcelona.org",
                "@type": "ContactPoint",
                "contactType": "Author",
                "email": "adam.hospital@irbbarcelona.org",
                "identifier": "adam.hospital@irbbarcelona.org",
                "url": "https://orcid.org/0000-0002-8291-8071"
            },
            {
                "@id": "https://ror.org/01z1gye03",
                "@type": "Organization",
                "name": "IRB Barcelona"
            },
            {
                "@id": "application_sources/matmul_directory.py",
                "@type": [
                    "File",
                    "SoftwareSourceCode",
                    "ComputationalWorkflow"
                ],
                "contentSize": 2163,
                "description": "Main file of the COMPSs workflow source files",
                "encodingFormat": "text/plain",
                "image": {
                    "@id": "complete_graph.svg"
                },
                "name": "matmul_directory.py",
                "programmingLanguage": {
                    "@id": "#compss"
                }
            },
            {
                "@id": "#compss",
                "@type": "ComputerLanguage",
                "alternateName": "COMPSs",
                "citation": "https://doi.org/10.1007/s10723-013-9272-5",
                "name": "COMPSs Programming Model",
                "url": "http://compss.bsc.es/",
                "version": "3.1.rc2305"
            },
            {
                "@id": "https://www.nationalarchives.gov.uk/PRONOM/fmt/92",
                "@type": "WebSite",
                "name": "Scalable Vector Graphics"
            },
            {
                "@id": "complete_graph.svg",
                "@type": [
                    "File",
                    "ImageObject",
                    "WorkflowSketch"
                ],
                "about": {
                    "@id": "application_sources/matmul_directory.py"
                },
                "contentSize": 6163,
                "description": "The graph diagram of the workflow, automatically generated by COMPSs runtime",
                "encodingFormat": [
                    [
                        "image/svg+xml",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/fmt/92"
                        }
                    ]
                ],
                "name": "complete_graph.svg"
            },
            {
                "@id": "https://www.nationalarchives.gov.uk/PRONOM/fmt/817",
                "@type": "WebSite",
                "name": "JSON Data Interchange Format"
            },
            {
                "@id": "App_Profile.json",
                "@type": "File",
                "contentSize": 357,
                "description": "COMPSs application Tasks profile",
                "encodingFormat": [
                    "application/json",
                    {
                        "@id": "https://www.nationalarchives.gov.uk/PRONOM/fmt/817"
                    }
                ],
                "name": "App_Profile.json"
            },
            {
                "@id": "compss_command_line_arguments.txt",
                "@type": "File",
                "contentSize": 24,
                "description": "COMPSs command line execution command, including parameters passed",
                "encodingFormat": "text/plain",
                "name": "compss_command_line_arguments.txt"
            },
            {
                "@id": "application_sources/matmul_tasks.py",
                "@type": [
                    "File",
                    "SoftwareSourceCode"
                ],
                "contentSize": 1721,
                "description": "Auxiliary File",
                "encodingFormat": "text/plain",
                "name": "matmul_tasks.py"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.0.0",
                "@type": "File",
                "contentSize": 16,
                "dateModified": "2023-05-16T14:29:04",
                "name": "A.0.0",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.0.1",
                "@type": "File",
                "contentSize": 16,
                "dateModified": "2023-05-16T14:29:04",
                "name": "A.0.1",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.1.0",
                "@type": "File",
                "contentSize": 16,
                "dateModified": "2023-05-16T14:29:04",
                "name": "A.1.0",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.1.1",
                "@type": "File",
                "contentSize": 16,
                "dateModified": "2023-05-16T14:29:04",
                "name": "A.1.1",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.0.0",
                "@type": "File",
                "contentSize": 16,
                "dateModified": "2023-05-16T14:29:04",
                "name": "B.0.0",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.0.1",
                "@type": "File",
                "contentSize": 16,
                "dateModified": "2023-05-16T14:29:04",
                "name": "B.0.1",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.1.0",
                "@type": "File",
                "contentSize": 16,
                "dateModified": "2023-05-16T14:29:04",
                "name": "B.1.0",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.1.1",
                "@type": "File",
                "contentSize": 16,
                "dateModified": "2023-05-16T14:29:04",
                "name": "B.1.1",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/",
                "@type": "Dataset",
                "dateModified": "2023-05-16T14:29:04",
                "hasPart": [
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.0.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.0.1"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.1.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.1.1"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.0.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.0.1"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.1.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.1.1"
                    }
                ],
                "name": "inputs",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.0.0",
                "@type": "File",
                "contentSize": 20,
                "dateModified": "2023-05-16T14:29:16",
                "name": "C.0.0",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.0.1",
                "@type": "File",
                "contentSize": 20,
                "dateModified": "2023-05-16T14:29:16",
                "name": "C.0.1",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.1.0",
                "@type": "File",
                "contentSize": 20,
                "dateModified": "2023-05-16T14:29:16",
                "name": "C.1.0",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.1.1",
                "@type": "File",
                "contentSize": 20,
                "dateModified": "2023-05-16T14:29:16",
                "name": "C.1.1",
                "sdDatePublished": "2023-05-16T14:29:25+00:00"
            },
            {
                "@id": "#COMPSs_Workflow_Run_Crate_bsccs742.int.bsc.es_aff79a2b-6487-4932-9e9b-eed5f31b2666",
                "@type": "CreateAction",
                "actionStatus": {
                    "@id": "http://schema.org/CompletedActionStatus"
                },
                "agent": {
                    "@id": "https://orcid.org/0000-0002-8291-8071"
                },
                "description": "Darwin bsccs742.int.bsc.es 22.4.0 Darwin Kernel Version 22.4.0: Mon Mar  6 21:00:17 PST 2023; root:xnu-8796.101.5~3/RELEASE_X86_64 x86_64 COMPSS_HOME=/Users/rsirvent/opt/COMPSs/",
                "endTime": "2023-05-16T14:29:25+00:00",
                "instrument": {
                    "@id": "application_sources/matmul_directory.py"
                },
                "name": "COMPSs matmul_directory.py execution at bsccs742.int.bsc.es",
                "object": [
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.0.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.0.1"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.1.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.1.1"
                    }
                ],
                "result": [
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.0.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.0.1"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.1.0"
                    },
                    {
                        "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.1.1"
                    },
                    {
                        "@id": "./"
                    }
                ]
            },
            {
                "@id": "https://w3id.org/ro/wfrun/process/0.1",
                "@type": "CreativeWork",
                "name": "Process Run Crate",
                "version": "0.1"
            },
            {
                "@id": "https://w3id.org/ro/wfrun/workflow/0.1",
                "@type": "CreativeWork",
                "name": "Workflow Run Crate",
                "version": "0.1"
            },
            {
                "@id": "https://w3id.org/workflowhub/workflow-ro-crate/1.0",
                "@type": "CreativeWork",
                "name": "Workflow RO-Crate",
                "version": "1.0"
            }
        ]
    }

ro-crate-metadata.json Java COMPSs example (MN4 supercomputer)
--------------------------------------------------------------

In this second ``ro-crate-metadata.json`` example, we want to illustrate the workflow provenance result of a Java COMPSs
application execution in the MareNostrum 4 supercomputer. We show the execution of a matrix LU factorization
for out-of-core sparse matrices implemented with COMPSs and using the Java programming language. In this algorithm,
matrix ``A`` is both input and output of the workflow, since the factorization overwrites the original value of ``A``.
In addition, we have used a 4x4 blocks hyper-matrix (i.e. the matrix is divided in 16 blocks, that contain 16
elements each) and, if a block is all 0s, the corresponding file will not be
created in the file system (in the example, this happens for blocks ``A.0.3``, ``A.1.3``, ``A.3.0`` and ``A.3.1``).

Apart from the terms already mentioned in the previous example (``creator``, ``publisher``, ``hasPart``,
``ComputationalWorkflow``, ``version``, ``CreateAction``), if we first observe the ``ro-crate-info.yaml`` file:

.. code-block:: yaml

    COMPSs Workflow Information:
      name: COMPSs Sparse LU
      description: The Sparse LU application computes an LU matrix factorization on a sparse blocked matrix. The matrix size (number of blocks) and the block size are parameters of the application.
      license: Apache-2.0 #Provide better a URL, but these strings are accepted:
                        # https://about.workflowhub.eu/Workflow-RO-Crate/#supported-licenses
      sources_dir: [src, jar, xml]
      files: [Readme, pom.xml, ro-crate-info.yaml]

    Authors:
      - name: Raül Sirvent
        e-mail: Raul.Sirvent@bsc.es
        orcid: https://orcid.org/0000-0003-0606-2512
        organisation_name: Barcelona Supercomputing Center
        ror: https://ror.org/05sd8tv96

We can see that we have specified several directories to be added as source files: the ``src`` folder that contains the
``.java`` and ``.class`` files, the ``jar`` folder with the ``sparseLU.jar`` file, and the ``xml`` folder with extra
xml configuration files. Besides, we also add the ``Readme``, ``pom.xml``, and the ``ro-crate-info.yaml`` file itself,
so they are packed in the resulting crate. This example also shows that the script is able to select the correct
``SparseLU.java`` main file as the ``ComputationalWorkflow`` in the RO-Crate, even when in the ``sources_dir`` three
files using the same file name exists (i.e. they implement 3 versions of the same algorithm: using files, arrays or
objects). Finally, since no ``Submitter`` is defined, the first author will be considered as such. The resulting
tree for the source files is:

.. code-block:: console

    application_sources/
    |-- Readme
    |-- jar
    |   `-- sparseLU.jar
    |-- pom.xml
    |-- ro-crate-info.yaml
    |-- src
    |   `-- main
    |       `-- java
    |           `-- sparseLU
    |               |-- arrays
    |               |   |-- SparseLU.class
    |               |   |-- SparseLU.java
    |               |   |-- SparseLUImpl.class
    |               |   |-- SparseLUImpl.java
    |               |   |-- SparseLUItf.class
    |               |   `-- SparseLUItf.java
    |               |-- files
    |               |   |-- Block.class
    |               |   |-- Block.java
    |               |   |-- SparseLU.class
    |               |   |-- SparseLU.java
    |               |   |-- SparseLUImpl.class
    |               |   |-- SparseLUImpl.java
    |               |   |-- SparseLUItf.class
    |               |   `-- SparseLUItf.java
    |               `-- objects
    |                   |-- Block.class
    |                   |-- Block.java
    |                   |-- SparseLU.class
    |                   |-- SparseLU.java
    |                   |-- SparseLUItf.class
    |                   `-- SparseLUItf.java
    `-- xml
        |-- project.xml
        `-- resources.xml

    9 directories, 26 files

It is also interesting to note the differences in the URIs used to reference input and output files when provenance is
run in a supercomputer, instead of a laptop (as shown in the previous example). Since we do not add explicitly the input
and output files of a workflow (because they could be extremely large), our crate only includes references to them,
which are ment as pointers to where files can be found, rather than a publicly accessible URI reference. Therefore,
while in the PyCOMPSs previous example files could be found in the ``bsccs742.int.bsc.es`` laptop, in this Java COMPSs
example files can be found in ``s08r2b16-ib0`` hostname, which is an internal hostname of MN4. This means that, for
reproducibility purposes, a new user would have to request input and output files to ``bsccs742.int.bsc.es``
laptop's owner in the first case, or request access to the MN4 paths specified by the corresponding URIs, in the
second case.

The ``CreateAction`` term has also a richer set of information available from MareNostrum's SLURM workload manager. We
can see that both the ``id`` and the ``description`` terms include the ``SLURM_JOB_ID``, which can be used to see more
details and statistics on the job run from SLURM using the `User Portal <https://userportal.bsc.es/>`_ tool. In addition, many more
environment variables are captured, which provide details on how the execution has been performed (i.e.
``SLURM_JOB_NODE_LIST``, ``SLURM_JOB_NUM_NODES``, ``SLURM_JOB_CPUS_PER_NODE``, ``COMPSS_MASTER_NODE``,
``COMPSS_WORKER_NODES``, among others).

.. code-block:: json

    {
        "@context": "https://w3id.org/ro/crate/1.1/context",
        "@graph": [
            {
                "@id": "./",
                "@type": "Dataset",
                "conformsTo": [
                    {
                        "@id": "https://w3id.org/ro/wfrun/process/0.1"
                    },
                    {
                        "@id": "https://w3id.org/ro/wfrun/workflow/0.1"
                    },
                    {
                        "@id": "https://w3id.org/workflowhub/workflow-ro-crate/1.0"
                    }
                ],
                "creator": [
                    {
                        "@id": "https://orcid.org/0000-0003-0606-2512"
                    }
                ],
                "datePublished": "2023-05-16T14:52:36+00:00",
                "description": "The Sparse LU application computes an LU matrix factorization on a sparse blocked matrix. The matrix size (number of blocks) and the block size are parameters of the application.",
                "hasPart": [
                    {
                        "@id": "application_sources/src/main/java/sparseLU/files/Block.java"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/files/SparseLUItf.class"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/files/SparseLUImpl.java"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/files/SparseLU.java"
                    },
                    {
                        "@id": "complete_graph.svg"
                    },
                    {
                        "@id": "App_Profile.json"
                    },
                    {
                        "@id": "compss_command_line_arguments.txt"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/files/Block.class"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/files/SparseLUItf.java"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/files/SparseLUImpl.class"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/files/SparseLU.class"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/objects/Block.java"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/objects/SparseLUItf.class"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/objects/SparseLU.java"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/objects/Block.class"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/objects/SparseLUItf.java"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/objects/SparseLU.class"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLUItf.class"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLUImpl.java"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLU.java"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLUItf.java"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLUImpl.class"
                    },
                    {
                        "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLU.class"
                    },
                    {
                        "@id": "application_sources/jar/sparseLU.jar"
                    },
                    {
                        "@id": "application_sources/xml/resources.xml"
                    },
                    {
                        "@id": "application_sources/xml/project.xml"
                    },
                    {
                        "@id": "application_sources/Readme"
                    },
                    {
                        "@id": "application_sources/pom.xml"
                    },
                    {
                        "@id": "application_sources/ro-crate-info.yaml"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.0"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.1"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.0"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.1"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.0"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.1"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.3"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.3.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.3.3"
                    }
                ],
                "license": "Apache-2.0",
                "mainEntity": {
                    "@id": "application_sources/src/main/java/sparseLU/files/SparseLU.java"
                },
                "mentions": {
                    "@id": "#COMPSs_Workflow_Run_Crate_marenostrum4_SLURM_JOB_ID_28492578"
                },
                "name": "COMPSs Sparse LU",
                "publisher": [
                    {
                        "@id": "https://ror.org/05sd8tv96"
                    }
                ]
            },
            {
                "@id": "ro-crate-metadata.json",
                "@type": "CreativeWork",
                "about": {
                    "@id": "./"
                },
                "conformsTo": [
                    {
                        "@id": "https://w3id.org/ro/crate/1.1"
                    },
                    {
                        "@id": "https://w3id.org/workflowhub/workflow-ro-crate/1.0"
                    }
                ]
            },
            {
                "@id": "https://orcid.org/0000-0003-0606-2512",
                "@type": "Person",
                "affiliation": {
                    "@id": "https://ror.org/05sd8tv96"
                },
                "contactPoint": {
                    "@id": "mailto:Raul.Sirvent@bsc.es"
                },
                "name": "Ra\u00fcl Sirvent"
            },
            {
                "@id": "mailto:Raul.Sirvent@bsc.es",
                "@type": "ContactPoint",
                "contactType": "Author",
                "email": "Raul.Sirvent@bsc.es",
                "identifier": "Raul.Sirvent@bsc.es",
                "url": "https://orcid.org/0000-0003-0606-2512"
            },
            {
                "@id": "https://ror.org/05sd8tv96",
                "@type": "Organization",
                "name": "Barcelona Supercomputing Center"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/files/Block.java",
                "@type": [
                    "File",
                    "SoftwareSourceCode"
                ],
                "contentSize": 5589,
                "description": "Auxiliary File",
                "encodingFormat": "text/plain",
                "name": "Block.java"
            },
            {
                "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/415",
                "@type": "WebSite",
                "name": "Java Compiled Object Code"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/files/SparseLUItf.class",
                "@type": "File",
                "contentSize": 904,
                "description": "Auxiliary File",
                "encodingFormat": [
                    [
                        "Java .class",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/415"
                        }
                    ]
                ],
                "name": "SparseLUItf.class"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/files/SparseLUImpl.java",
                "@type": [
                    "File",
                    "SoftwareSourceCode"
                ],
                "contentSize": 2431,
                "description": "Auxiliary File",
                "encodingFormat": "text/plain",
                "name": "SparseLUImpl.java"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/files/SparseLU.java",
                "@type": [
                    "File",
                    "SoftwareSourceCode",
                    "ComputationalWorkflow"
                ],
                "contentSize": 6602,
                "description": "Main file of the COMPSs workflow source files",
                "encodingFormat": "text/plain",
                "image": {
                    "@id": "complete_graph.svg"
                },
                "name": "SparseLU.java",
                "programmingLanguage": {
                    "@id": "#compss"
                }
            },
            {
                "@id": "#compss",
                "@type": "ComputerLanguage",
                "alternateName": "COMPSs",
                "citation": "https://doi.org/10.1007/s10723-013-9272-5",
                "name": "COMPSs Programming Model",
                "url": "http://compss.bsc.es/",
                "version": "3.1.rc2305"
            },
            {
                "@id": "https://www.nationalarchives.gov.uk/PRONOM/fmt/92",
                "@type": "WebSite",
                "name": "Scalable Vector Graphics"
            },
            {
                "@id": "complete_graph.svg",
                "@type": [
                    "File",
                    "ImageObject",
                    "WorkflowSketch"
                ],
                "about": {
                    "@id": "application_sources/src/main/java/sparseLU/files/SparseLU.java"
                },
                "contentSize": 21106,
                "description": "The graph diagram of the workflow, automatically generated by COMPSs runtime",
                "encodingFormat": [
                    [
                        "image/svg+xml",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/fmt/92"
                        }
                    ]
                ],
                "name": "complete_graph.svg"
            },
            {
                "@id": "https://www.nationalarchives.gov.uk/PRONOM/fmt/817",
                "@type": "WebSite",
                "name": "JSON Data Interchange Format"
            },
            {
                "@id": "App_Profile.json",
                "@type": "File",
                "contentSize": 1584,
                "description": "COMPSs application Tasks profile",
                "encodingFormat": [
                    "application/json",
                    {
                        "@id": "https://www.nationalarchives.gov.uk/PRONOM/fmt/817"
                    }
                ],
                "name": "App_Profile.json"
            },
            {
                "@id": "compss_command_line_arguments.txt",
                "@type": "File",
                "contentSize": 28,
                "description": "COMPSs command line execution command, including parameters passed",
                "encodingFormat": "text/plain",
                "name": "compss_command_line_arguments.txt"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/files/Block.class",
                "@type": "File",
                "contentSize": 4135,
                "description": "Auxiliary File",
                "encodingFormat": [
                    [
                        "Java .class",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/415"
                        }
                    ]
                ],
                "name": "Block.class"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/files/SparseLUItf.java",
                "@type": [
                    "File",
                    "SoftwareSourceCode"
                ],
                "contentSize": 1808,
                "description": "Auxiliary File",
                "encodingFormat": "text/plain",
                "name": "SparseLUItf.java"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/files/SparseLUImpl.class",
                "@type": "File",
                "contentSize": 1310,
                "description": "Auxiliary File",
                "encodingFormat": [
                    [
                        "Java .class",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/415"
                        }
                    ]
                ],
                "name": "SparseLUImpl.class"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/files/SparseLU.class",
                "@type": "File",
                "contentSize": 4682,
                "description": "Auxiliary File",
                "encodingFormat": [
                    [
                        "Java .class",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/415"
                        }
                    ]
                ],
                "name": "SparseLU.class"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/objects/Block.java",
                "@type": [
                    "File",
                    "SoftwareSourceCode"
                ],
                "contentSize": 4345,
                "description": "Auxiliary File",
                "encodingFormat": "text/plain",
                "name": "Block.java"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/objects/SparseLUItf.class",
                "@type": "File",
                "contentSize": 816,
                "description": "Auxiliary File",
                "encodingFormat": [
                    [
                        "Java .class",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/415"
                        }
                    ]
                ],
                "name": "SparseLUItf.class"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/objects/SparseLU.java",
                "@type": [
                    "File",
                    "SoftwareSourceCode"
                ],
                "contentSize": 4740,
                "description": "Auxiliary File",
                "encodingFormat": "text/plain",
                "name": "SparseLU.java"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/objects/Block.class",
                "@type": "File",
                "contentSize": 2991,
                "description": "Auxiliary File",
                "encodingFormat": [
                    [
                        "Java .class",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/415"
                        }
                    ]
                ],
                "name": "Block.class"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/objects/SparseLUItf.java",
                "@type": [
                    "File",
                    "SoftwareSourceCode"
                ],
                "contentSize": 1529,
                "description": "Auxiliary File",
                "encodingFormat": "text/plain",
                "name": "SparseLUItf.java"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/objects/SparseLU.class",
                "@type": "File",
                "contentSize": 3403,
                "description": "Auxiliary File",
                "encodingFormat": [
                    [
                        "Java .class",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/415"
                        }
                    ]
                ],
                "name": "SparseLU.class"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLUItf.class",
                "@type": "File",
                "contentSize": 808,
                "description": "Auxiliary File",
                "encodingFormat": [
                    [
                        "Java .class",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/415"
                        }
                    ]
                ],
                "name": "SparseLUItf.class"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLUImpl.java",
                "@type": [
                    "File",
                    "SoftwareSourceCode"
                ],
                "contentSize": 4114,
                "description": "Auxiliary File",
                "encodingFormat": "text/plain",
                "name": "SparseLUImpl.java"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLU.java",
                "@type": [
                    "File",
                    "SoftwareSourceCode"
                ],
                "contentSize": 4840,
                "description": "Auxiliary File",
                "encodingFormat": "text/plain",
                "name": "SparseLU.java"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLUItf.java",
                "@type": [
                    "File",
                    "SoftwareSourceCode"
                ],
                "contentSize": 1899,
                "description": "Auxiliary File",
                "encodingFormat": "text/plain",
                "name": "SparseLUItf.java"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLUImpl.class",
                "@type": "File",
                "contentSize": 2430,
                "description": "Auxiliary File",
                "encodingFormat": [
                    [
                        "Java .class",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/415"
                        }
                    ]
                ],
                "name": "SparseLUImpl.class"
            },
            {
                "@id": "application_sources/src/main/java/sparseLU/arrays/SparseLU.class",
                "@type": "File",
                "contentSize": 3304,
                "description": "Auxiliary File",
                "encodingFormat": [
                    [
                        "Java .class",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/415"
                        }
                    ]
                ],
                "name": "SparseLU.class"
            },
            {
                "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/412",
                "@type": "WebSite",
                "name": "Java Archive Format"
            },
            {
                "@id": "application_sources/jar/sparseLU.jar",
                "@type": "File",
                "contentSize": 28758,
                "description": "Auxiliary File",
                "encodingFormat": [
                    [
                        "application/java-archive",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/x-fmt/412"
                        }
                    ]
                ],
                "name": "sparseLU.jar"
            },
            {
                "@id": "application_sources/xml/resources.xml",
                "@type": "File",
                "contentSize": 983,
                "description": "Auxiliary File",
                "name": "resources.xml"
            },
            {
                "@id": "application_sources/xml/project.xml",
                "@type": "File",
                "contentSize": 289,
                "description": "Auxiliary File",
                "name": "project.xml"
            },
            {
                "@id": "application_sources/Readme",
                "@type": "File",
                "contentSize": 1935,
                "description": "Auxiliary File",
                "name": "Readme"
            },
            {
                "@id": "application_sources/pom.xml",
                "@type": "File",
                "contentSize": 4454,
                "description": "Auxiliary File",
                "name": "pom.xml"
            },
            {
                "@id": "application_sources/ro-crate-info.yaml",
                "@type": "File",
                "contentSize": 699,
                "description": "Auxiliary File",
                "name": "ro-crate-info.yaml"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.0",
                "@type": "File",
                "contentSize": 304,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.0.0",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.1",
                "@type": "File",
                "contentSize": 303,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.0.1",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.2",
                "@type": "File",
                "contentSize": 306,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.0.2",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.0",
                "@type": "File",
                "contentSize": 311,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.1.0",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.1",
                "@type": "File",
                "contentSize": 320,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.1.1",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.2",
                "@type": "File",
                "contentSize": 312,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.1.2",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.0",
                "@type": "File",
                "contentSize": 319,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.2.0",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.1",
                "@type": "File",
                "contentSize": 323,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.2.1",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.2",
                "@type": "File",
                "contentSize": 311,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.2.2",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.3",
                "@type": "File",
                "contentSize": 303,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.2.3",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.3.2",
                "@type": "File",
                "contentSize": 320,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.3.2",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.3.3",
                "@type": "File",
                "contentSize": 310,
                "dateModified": "2023-05-16T14:52:35",
                "name": "A.3.3",
                "sdDatePublished": "2023-05-16T14:52:36+00:00"
            },
            {
                "@id": "#COMPSs_Workflow_Run_Crate_marenostrum4_SLURM_JOB_ID_28492578",
                "@type": "CreateAction",
                "actionStatus": {
                    "@id": "http://schema.org/CompletedActionStatus"
                },
                "agent": {
                    "@id": "https://orcid.org/0000-0003-0606-2512"
                },
                "description": "Linux s08r2b16 4.4.59-92.20-default #1 SMP Wed May 31 14:05:24 UTC 2017 (8cd473d) x86_64 x86_64 x86_64 GNU/Linux SLURM_JOB_NAME=sparseLU-java-DP SLURM_JOB_QOS=debug SLURM_MEM_PER_CPU=1880 SLURM_JOB_ID=28492578 SLURM_JOB_USER=bsc19057 COMPSS_HOME=/apps/COMPSs/3.2.pr/ SLURM_JOB_UID=2952 SLURM_SUBMIT_DIR=/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU SLURM_JOB_NODELIST=s08r2b[16,20] SLURM_JOB_GID=2950 SLURM_JOB_CPUS_PER_NODE=48(x2) COMPSS_MPIRUN_TYPE=impi SLURM_SUBMIT_HOST=login3 SLURM_JOB_PARTITION=main SLURM_JOB_ACCOUNT=bsc19 SLURM_JOB_NUM_NODES=2 COMPSS_MASTER_NODE=s08r2b16 COMPSS_WORKER_NODES= s08r2b20",
                "endTime": "2023-05-16T14:52:36+00:00",
                "instrument": {
                    "@id": "application_sources/src/main/java/sparseLU/files/SparseLU.java"
                },
                "name": "COMPSs SparseLU.java execution at marenostrum4 with JOB_ID 28492578",
                "object": [
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.0"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.1"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.0"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.1"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.0"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.1"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.3"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.3.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.3.3"
                    }
                ],
                "result": [
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.0"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.1"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.0.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.0"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.1"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.1.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.0"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.1"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.2.3"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.3.2"
                    },
                    {
                        "@id": "file://s08r2b16-ib0/gpfs/home/bsc19/bsc19057/COMPSs-DP/tutorial_apps/java/sparseLU/A.3.3"
                    },
                    {
                        "@id": "./"
                    }
                ],
                "subjectOf": [
                    "https://userportal.bsc.es/"
                ]
            },
            {
                "@id": "https://w3id.org/ro/wfrun/process/0.1",
                "@type": "CreativeWork",
                "name": "Process Run Crate",
                "version": "0.1"
            },
            {
                "@id": "https://w3id.org/ro/wfrun/workflow/0.1",
                "@type": "CreativeWork",
                "name": "Workflow Run Crate",
                "version": "0.1"
            },
            {
                "@id": "https://w3id.org/workflowhub/workflow-ro-crate/1.0",
                "@type": "CreativeWork",
                "name": "Workflow RO-Crate",
                "version": "1.0"
            }
        ]
    }
