Data Provenance
===============

In order to achieve **Reproducibility** and **Replicability** with your experiments
using COMPSs, the runtime includes the capacity of recording details of the
application's execution, also known as *Data Provenance*. This is supported for both Python
and Java applications.

When the provenance option is activated, the runtime records every access
to a file or directory in the application, as well as its direction (IN, 
OUT, INOUT). In addition to this, other information such as the parameters passed as inputs in the command line
that submitted the application, its source files, workflow image and profiling statistics, authors and
their institutions, ... are also stored.
All this information is later used to record the Data Provenance
of your workflow using the `RO-Crate specification <https://www.researchobject.org/ro-crate/1.1/>`_, and with the assistance of
the `ro-crate-py library <https://github.com/ResearchObject/ro-crate-py>`_. RO-Crate is based on
JSON-LD (JavaScript Object Notation for Linked Data), is
much simpler than other standards and tools created to record Provenance, and
that is why it has been adopted in a number of communities. Using RO-Crate
to register the execution's information ensures
not only to register correctly the Provenance of a COMPSs application run, but
also compatibility with some existing portals that already embrace
RO-Crate as their core format for representing metadata, such as `WorkflowHub <https://workflowhub.eu/>`_.


Software dependencies
---------------------

Provenance generation in COMPSs depends on the `ro-crate-py library <https://github.com/ResearchObject/ro-crate-py>`_,
thus, it must be installed before the provenance option can be used. Depending on the target system, different
options are available using ``pip``:

If the installation is in a laptop or machine you manage, you can use the command:

.. code-block:: console

    compss@bsc:~$ pip install rocrate

If you do not manage the target machine, you can install the library in your own user space using:

.. code-block:: console

    compss@bsc:~$ pip install rocrate --user

This would typically install the library in ``~/.local/``. Another option is to specify the target directory with:

.. code-block:: console

    compss@bsc:~$ pip install -t install_path rocrate

Our implementation has been tested with ``ro-crate-py`` version ``0.7.0`` and earlier.


Previous needed information
---------------------------

There are certain pieces of information which must be included when registering the provenance of a workflow that
the COMPSs runtime cannot automatically infer, such as the authors of an application. For specifying all these
fields that are needed to generate an RO-Crate but cannot be automatically obtained, we have created a simple YAML
structure where the user can specify them. They need to provide in their working directory (i.e., where the application
is going to be run) a YAML file named ``ro-crate-info.yaml`` that follows the next template structure:

.. code-block:: yaml

    COMPSs Workflow Information:
      name: Name of your COMPSs application
      description: Detailed description of your COMPSs application
      license: Apache-2.0 #Provide better a URL, but these strings are accepted:
                      # https://about.workflowhub.eu/Workflow-RO-Crate/#supported-licenses
      sources_dir: [path_to/dir_1, path_to/dir_2]  # Optional: List of directories containing the application source files.
            # Relative or absolute paths can be used
      sources_main_file: my_main_file.py  # Optional: Name of the main file of the application, located in one of the
            # sources_dir. Relative paths from a sources_dir entry, or absolute paths can be used
      files: [main_file.py, aux_file_1.py, aux_file_2.py] # List of application files
            # Relative or absolute paths can be used
    Authors:
      - name: Author_1 Name
        e-mail: author_1@email.com
        orcid: https://orcid.org/XXXX-XXXX-XXXX-XXXX
        organisation_name: Institution_1 name
        ror: https://ror.org/XXXXXXXXX # Find them in ror.org
      - name: Author_2 Name
        e-mail: author2@email.com
        orcid: https://orcid.org/YYYY-YYYY-YYYY-YYYY
        organisation_name: Institution_2 name
        ror: https://ror.org/YYYYYYYYY # Find them in ror.org

.. WARNING::

    If no YAML file is provided, the runtime will fail to generate provenance, and will automatically generate an
    ``ro-crate-info_TEMPLATE.yaml`` file that the user can edit to add their details.

As you can see, there are two main blocks in the YAML:

- **COMPSs Workflow Information:** Where details on the application are provided.

- **Authors:** Where authors' details are given.

More specifically, in the **COMPSs Workflow Information** section:

- The ``name`` and ``description`` fields are free text, where a long name and description of
  the application must be provided.

- The ``license`` field is preferred by providing an URL to the license, but a set of
  predefined strings are also supported, and can be found here:
  https://about.workflowhub.eu/Workflow-RO-Crate/#supported-licenses

- ``sources_dir`` can be a single path, or a list of paths where application source files can be found. Our script
  will add ALL files (i.e., not only source files, but any file found) and sub-directories inside each of the paths
  specified. The sub-directories structure is respected
  when the files are added in the crate (in a sub-directory ``application_sources``).

- ``sources_main_file`` is the name of the main source file of the application, and may be used if the user wants to specify
  a particular file as such. The COMPSs runtime detects automatically the main source of an application, therefore this is a way
  to override the detected file. The file can be specified with only its name or a relative path inside one of the
  directories listed in ``sources_dir``. An absolute path can also be used.

- ``files`` is a single or a list of all the source files of the application (typically all ``.py`` files for Python
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

And in the **Authors** section:

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

In the following lines, we provide a YAML example for an out-of-core Matrix Multiplication PyCOMPSs application,
distributed with license Apache v2.0, with 2 source files, and authored by 3 persons from two different
institutions.

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
We add to the crate the sub-directories that contain the ``.jar`` and ``.java`` files correspondingly.

.. code-block:: yaml

    COMPSs Workflow Information:
      name: COMPSs K-means
      description: K-means clustering is a method of cluster analysis that aims to partition ''n'' points into ''k''
        clusters in which each point belongs to the cluster with the nearest mean. It follows an iterative refinement
        strategy to find the centers of natural clusters in the data.
      license: https://opensource.org/licenses/Apache-2.0 #Provide better a URL, but these strings are accepted:
                        # https://about.workflowhub.eu/Workflow-RO-Crate/#supported-licenses
      sources_dir: [jar, src]

    Authors:
      - name: Raül Sirvent
        e-mail: Raul.Sirvent@bsc.es
        orcid: https://orcid.org/0000-0003-0606-2512
        organisation_name: Barcelona Supercomputing Center
        ror: https://ror.org/05sd8tv96

Usage
-----

The way of activating the recording of Data Provenance with COMPSs is very simple.
One must only enable the ``-p`` or ``--provenance`` flag when using ``runcomps`` or
``enqueue_compss`` to run or submit a COMPSs application respectively.
As shown in the help option:
 
.. code-block:: console

    compss@bsc:~$ runcompss -h

    (...)
    --provenance, -p    Generate COMPSs workflow provenance data in RO-Crate format from YAML file. Automatically
                        activates -graph and -output_profile.
                        Default: false

.. WARNING::

    As stated in the help, provenance automatically activates both ``--graph`` and ``--output_profile`` options.
    Take into account that the graph image generation can take some extra seconds at the end of the execution of your
    application, therefore, adjust the ``--exec_time`` accordingly.

In the case of extremely large workflows (e.g., a workflow
with tenths of thousands of task nodes, or tenths of thousands of files used as inputs or outputs), the extra time
needed to generate the data provenance with RO-Crate may be a problem in systems with strict run time constraints.
In these cases, the workflow execution may end correctly, but the extra processing to generate the provenance may be killed
by the system if it exceeds a certain limit, and the provenance will not be created correctly.

For this or any other similar situation, our data provenance generation script can be triggered offline at any moment
after the workflow has executed correctly, thanks to our design. From the working directory of the application, the
following commands may be used:

.. code-block:: console

    compss@bsc:~$ $COMPSS_HOME/Runtime/scripts/utils/compss_gengraph svg $BASE_LOG_DIR/monitor/complete_graph.dot

    compss@bsc:~$ python $COMPSS_HOME/Runtime/scripts/system/provenance/generate_COMPSs_RO-Crate.py ro-crate-info.yaml $BASE_LOG_DIR/dataprovenance.log

In these commands, ``COMPSS_HOME`` is where your COMPSs installation is located, and ``BASE_LOG_DIR`` points to the path where the
application run logs are stored (see Section :ref:`Sections/03_Execution_Environments/03_Deployments/01_Master_worker/01_Local/02_Results_and_logs:Logs`
for more details on where to locate these logs). ``compss_gengraph``
generates the workflow image to be added to the crate, but if its generation time is a concern, or the user does not
want it to be included in the crate, the command can be skipped. The second command runs the
``generate_COMPSs_RO-Crate.py`` Python script, that uses the information provided by the user in ``ro-crate-info.yaml``
combined with the file accesses information registered by the COMPSs runtime in the ``dataprovenance.log`` file. The
result is a sub-directory ``COMPSs_RO-Crate_[uuid]/`` that contains the data provenance of the run (see next sub-section
for a detailed description).

# More details can be obtained in the WORKS 22 paper...

Result
------

Once the application has finished, a new sub-folder under the application's Working Directory
will be created with the name ``COMPSs_RO-Crate_[uuid]/``, which is also known as *crate*. The contents of the
folder include all the elements needed to reproduce a COMPSs execution, and
are:

- **Application Source Files:** As detailed by the user in the ``ro-crate-info.yaml`` file
  with the terms ``sources_dir`` and/or ``files``. They have to include
  the main source file and all auxiliary files that the application needs (e.g.: ``.py``, .``.java``, ``.class``
  or ``.jar``). Optionally, the term ``sources_main_file`` can be used to manually select the main source file of
  the application. All application files are added to a sub-folder in the crate named ``application_sources``, where
  the ``sources_dir`` locations are included with their same folder tree structure. The files included with the
  ``files`` term are added to the root of the ``application_sources`` sub-folder in the crate.

- **complete_graph.svg:** The image of the workflow generated by the COMPSs runtime,
  as generated with the ``runcompss -g`` or ``--graph`` option.

- **App_Profile.json:** A set of statistics of the application run recorded by the
  COMPSs runtime, as if the ``runcompss --output_profile=<path>`` option was enabled.
  It includes, for each resource and method executed: number of executions of the
  specific method, as well as maximum, average and minimum run time.

- **compss_command_line_arguments.txt:** Stores the options passed by the command
  line when the application was submitted. This is very important for reproducing a COMPSs
  application, since input parameters could potentially change the resulting workflow generated
  by the COMPSs runtime.

- **ro-crate-metadata.json:** The RO-Crate JSON main file describing the contents of
  this directory (crate) in the RO-Crate specification format. You can find an example at the end of this Section.

.. WARNING::

    All previous file names (``complete_graph.svg``, ``App_Profile.json`` and ``compss_command_line_arguments.txt``)
    are automatically used to generate new files when using the ``-p`` or ``--provenance`` option.
    Avoid using these file names among
    your own files to avoid unwanted overwritings. You can change the resulting ``App_Profile.json`` name by using
    the ``--output_profile=/path_to/file`` flag.


ro-crate-metadata.json example
------------------------------

In the RO-Crate specification, the root file containing the metadata referring to the crate created is named
``ro-crate-metadata.json``. In these lines we provide an example of an ro-crate-metadata.json file resulting from
a COMPSs application execution, specifically an out-of-core matrix multiplication example that includes matrices
``A`` and ``B`` as inputs in an ``inputs/`` sub-directory, and matrix ``C`` as the result of their multiplication.
For all the specific details on the fields provided in the JSON file, please refer to the
`RO-Crate specification Website <https://www.researchobject.org/ro-crate/1.1/>`_. Intuitively, if you search through
the JSON file you can find several interesting fields:

- **creator:** List of authors, identified by their ORCID.

- **publisher:** Organisations of the authors.

- **hasPart in ./:** lists all the files and directories this workflow needs and generates, and also the ones
  included in the crate. The URIs point to the local machine where the application has been run, thus, tells
  the user where the inputs and outputs can be found (in this example, a BSC laptop).

- **matmul_directory.py:** Main file of the application, includes the ``inputs`` and ``outputs`` needed and generated
  by the workflow, and a reference to the generated workflow image in the ``image`` field.

- **version:** The COMPSs specific version and build used to run this application. In the example: ``2.10.rc2205``.
  This is a very important field to achieve reproducibility or replicability, since COMPSs features may vary their
  behaviour in different versions of the programming model runtime.

We encourage the reader to navigate through this ``ro-crate-metadata.json`` file example to get familiar with its
contents. Many of the fields are easily and directly understandable.

.. code-block:: json

    {
        "@context": "https://w3id.org/ro/crate/1.1/context",
        "@graph": [
            {
                "@id": "./",
                "@type": "Dataset",
                "creator": [
                    {
                        "@id": "https://orcid.org/0000-0003-0606-2512"
                    },
                    {
                        "@id": "https://orcid.org/0000-0003-2941-5499"
                    },
                    {
                        "@id": "https://orcid.org/0000-0002-8291-8071"
                    }
                ],
                "datePublished": "2022-05-16T08:59:20+00:00",
                "description": "Hypermatrix size 2x2 blocks, block size 2x2 elements",
                "hasPart": [
                    {
                        "@id": "matmul_directory.py"
                    },
                    {
                        "@id": "complete_graph.pdf"
                    },
                    {
                        "@id": "App_Profile.json"
                    },
                    {
                        "@id": "compss_command_line_arguments.txt"
                    },
                    {
                        "@id": "matmul_tasks.py"
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
                    "@id": "matmul_directory.py"
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
                "@id": "matmul_directory.py",
                "@type": [
                    "File",
                    "SoftwareSourceCode",
                    "ComputationalWorkflow"
                ],
                "contentSize": 2151,
                "description": "Main file of the COMPSs workflow source files",
                "encodingFormat": "text/plain",
                "image": {
                    "@id": "complete_graph.pdf"
                },
                "input": [
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
                "name": "matmul_directory.py",
                "output": [
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
                "version": "2.10.rc2205"
            },
            {
                "@id": "https://www.nationalarchives.gov.uk/PRONOM/fmt/276",
                "@type": "WebSite",
                "name": "Acrobat PDF 1.7 - Portable Document Format"
            },
            {
                "@id": "complete_graph.pdf",
                "@type": [
                    "File",
                    "ImageObject",
                    "WorkflowSketch"
                ],
                "about": {
                    "@id": "matmul_directory.py"
                },
                "contentSize": 19582,
                "description": "The graph diagram of the workflow, automatically generated by COMPSs runtime",
                "encodingFormat": [
                    [
                        "application/pdf",
                        {
                            "@id": "https://www.nationalarchives.gov.uk/PRONOM/fmt/276"
                        }
                    ]
                ],
                "name": "complete_graph.pdf"
            },
            {
                "@id": "https://www.nationalarchives.gov.uk/PRONOM/fmt/817",
                "@type": "WebSite",
                "name": "JSON Data Interchange Format"
            },
            {
                "@id": "App_Profile.json",
                "@type": "File",
                "contentSize": 246,
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
                "contentSize": 4,
                "description": "Parameters passed as arguments to the COMPSs application through the command line",
                "encodingFormat": "text/plain",
                "name": "compss_command_line_arguments.txt"
            },
            {
                "@id": "matmul_tasks.py",
                "@type": "File",
                "contentSize": 1721,
                "description": "Auxiliary File",
                "encodingFormat": "text/plain",
                "name": "matmul_tasks.py"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.0.0",
                "@type": "File",
                "contentSize": 16,
                "name": "A.0.0",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.0.1",
                "@type": "File",
                "contentSize": 16,
                "name": "A.0.1",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.1.0",
                "@type": "File",
                "contentSize": 16,
                "name": "A.1.0",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/A/A.1.1",
                "@type": "File",
                "contentSize": 16,
                "name": "A.1.1",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.0.0",
                "@type": "File",
                "contentSize": 16,
                "name": "B.0.0",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.0.1",
                "@type": "File",
                "contentSize": 16,
                "name": "B.0.1",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.1.0",
                "@type": "File",
                "contentSize": 16,
                "name": "B.1.0",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/B/B.1.1",
                "@type": "File",
                "contentSize": 16,
                "name": "B.1.1",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/inputs/",
                "@type": "Dataset",
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
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.0.0",
                "@type": "File",
                "contentSize": 20,
                "name": "C.0.0",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.0.1",
                "@type": "File",
                "contentSize": 20,
                "name": "C.0.1",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.1.0",
                "@type": "File",
                "contentSize": 20,
                "name": "C.1.0",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
            {
                "@id": "file://bsccs742.int.bsc.es/Users/rsirvent/COMPSs-DP/matmul_directory/C.1.1",
                "@type": "File",
                "contentSize": 20,
                "name": "C.1.1",
                "sdDatePublished": "2022-05-16T08:59:20+00:00"
            },
        ]
    }
