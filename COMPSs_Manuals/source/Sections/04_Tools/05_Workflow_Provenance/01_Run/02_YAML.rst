.. _yaml-config:

YAML configuration file
=======================

There are certain pieces of information which must be included when registering the provenance of a workflow that
the COMPSs runtime cannot automatically infer, such as the authors of an application. For specifying all these
fields that are needed to generate an RO-Crate but cannot be automatically obtained, we have created a simple YAML
structure where the user can specify them. By default, a YAML file named ``ro-crate-info.yaml`` will be expected in the
working directory (i.e. where the application is going to be run), but a different YAML file can be used by specifying
it with ``--provenance=my_yaml_file.yaml`` when activating workflow provenance generation.
The YAML file must follow the next template structure (notice later that only one term is mandatory, some other terms
are commonly used, and the rest of terms are for special cases only):

.. code-block:: yaml

    COMPSs Workflow Information:
      name: Name of your COMPSs application
      description: Detailed description of your COMPSs application
      license: YourLicense-1.0
      sources: [/absolute_path_to/dir_1/, relative_path_to/dir_2/, main_file.py, relative_path/aux_file_1.py, /abs_path/aux_file_2.py]
      data_persistence: False
      trace_persistence: False
      software:
        - name: Software 1 name
          version: 1.1.1
          url: https://software1.org/
        - name: Software 2 name
          version: Software version description 2.2.2
          url: https://software2.org/

      # Optional, less commonly used
      inputs: [/abs_path_to/dir_1, rel_path_to/dir_2, file_1, rel_path/file_2, https://domain.to/file]
      outputs: [/abs_path_to/dir_1, rel_path_to/dir_2, file_1, rel_path/file_2, https://domain.to/file]
      sources_main_file: my_main_file.py

    Authors:
      - name: Author_1 Name
        e-mail: author_1@email.com
        orcid: https://orcid.org/XXXX-XXXX-XXXX-XXXX
        organisation_name: Institution_1 name
        ror: https://ror.org/XXXXXXXXX
      - name: Author_2 Name
        e-mail: author2@email.com
        orcid: https://orcid.org/YYYY-YYYY-YYYY-YYYY
        organisation_name: Institution_2 name
        ror: https://ror.org/YYYYYYYYY

    Agent:
      name: Name
      e-mail: agent@email.com
      orcid: https://orcid.org/XXXX-XXXX-XXXX-XXXX
      organisation_name: Agent Institution name
      ror: https://ror.org/XXXXXXXXX

.. WARNING::

    If no YAML file is provided, the runtime will fail to generate provenance, and will automatically generate an
    ``ro-crate-info_TEMPLATE.yaml`` file that the user can edit to add their details.

As you can see, there are three main blocks in the YAML:

- **COMPSs Workflow Information:** where details on the application are provided.

- **Authors:** where authors' details are given.

- **Agent:** the single person running the workflow in the computing resources.

COMPSs Workflow Information section
-----------------------------------

More specifically, in the **COMPSs Workflow Information** section, the most commonly used terms are:

- The ``name`` and ``description`` fields are free text, where a long name and long description of
  the application can be provided.

- ``sources`` can be a single directory or file, or a list of directories or files where application source
  files can be found. The ``sources`` term here is used not only to describe files with source code (typically all
  ``.py`` files for Python applications, or ``.java``, ``.class``, ``.jar`` files for Java ones), but also any
  installation and configuration scripts, compilation scripts (Makefile, pom.xml, ...), submission scripts, readme
  files, ... that should be included with the application package. Our script
  will add ALL files (i.e. not only source files, but any file found) and sub-directories inside each of the directory
  paths specified. The sub-directories structure is respected
  when the files are added in the crate (inside a sub-directory ``application_sources/``). Both
  relative and absolute paths can be used. If the term ``sources`` is not specified, only the application's main file
  will be added as the corresponding source code if it can be found in the current working directory.

- The ``license`` field is preferred to be specified by providing an URL to the license, but a set of
  predefined strings are also supported, and can be found at the `SPDX License list site <https://spdx.org/licenses/>`_.

- ``data_persistence`` value is ``False`` by default. It is a boolean to indicate whether the workflow provenance
  generation should copy the workflow's input and output datasets to the crate (i.e. must be set to ``True``).
  Including the datasets is feasible for workflows where they are small enough to be sent back and forth between
  execution environments. When datasets are too large to be moved around (i.e. hundreds of MB), this field should be set
  to ``False``.

- ``trace_persistence`` value is ``False`` by default. Whenever a Paraver trace is generated when running an experiment
  (see Section :ref:`Sections/04_Tools/03_Tracing/01_Apps_tracing:Activate Tracing`), the metadata of the resulting trace will be automatically
  added to the crate. As with datasets, the user can decide if the trace files themselves must be physically added, or
  include only references to where they can be located. If trace files are included, a directory named ``trace/`` will
  be available from the root path of the crate.

- ``software`` is used to manually describe the list of software dependencies (i.e. ``softwareRequirements`` in RO-Crate
  specification) this application
  has in order to be executed correctly. If the application requires certain packages / libraries / tools, they should be declared
  in this section. With this information recorded, metadata consumers will be able to react and install / load automatically
  these dependencies whenever a re-execution of the application is intended.

      - ``name`` is the full name of the external software used.
      - ``version`` can be a canonical version only (i.e. ``3.2.1``), or a much larger description (text).
        This should commonly include the output of ``tool --version`` command.
      - ``url`` where the software can be found.

From all these terms described, only ``name`` is  mandatory, since the rest are not strictly required to generate workflow provenance with COMPSs.
However, it is important to include as much information as possible in order to correctly share your application and
results. Besides, missing information can lead to reduced features when using workflow provenance (e.g. if no ``Authors``
are specified, WorkflowHub will not allow to generate a DOI for the workflow execution).

.. TIP::

    It is very important that the ``sources`` term is correctly defined, since the
    runtime will only register information for the list of source files defined under this term.

.. TIP::
    Large datasets (i.e. hundreds of MBs) should be uploaded to public
    data repositories (e.g. `Zenodo <https://zenodo.org/>`_ up to 50 GB per dataset, `FigShare <https://figshare.com/>`_
    up to 5 TB per dataset) and included as ``https`` references with the ``inputs`` or ``outputs`` terms.

.. WARNING::

    When ``data_persistence`` is True, application datasets will be stored in a ``dataset/`` sub-directory in the resulting
    crate. The sub-folder structure will be build starting at the largest possible common path among files (e.g. if ``/path_1/inputs/A/A.txt``
    and ``/path_1/inputs/B/B.txt`` are used, they will be located at ``dataset/inputs/A/A.txt`` and ``dataset/inputs/B/B.txt``
    respectively. However, if ``/path_1/inputs/A/A.txt`` and ``/path_2/inputs/B/B.txt`` are used, the location will be
    ``dataset/A.txt`` and ``dataset/B.txt``, since files do not share a common path and are considered to be at different
    locations.

Also, some more optional terms are available, but less commonly used:

- ``inputs`` to manually include input parameters (files or directories) to the application, in addition to the ones
  detected. In order to include very large files in the crate without actually copying them, files from remote
  repositories can be referenced (e.g. ``https://zenodo.org/records/10782431/files/lysozyme_datasets.zip``)

- ``outputs`` to manually include output parameters (files or directories) to the application, in addition to the ones
  detected. In order to include very large files in the crate without actually copying them, files from remote
  repositories can be referenced (e.g. ``https://zenodo.org/records/10783183/files/results_2003_0521_boumardes_BS.tar.gz``)

- ``sources_main_file`` is an advanced feature very rarely used, to override the detected main file for the application.
  It defines the name of the main source file of the application, and may be specified if the user wants to select
  a particular file as such. The COMPSs runtime detects automatically the main source of an application, therefore, this is a way
  to override the detected file. The file can be specified with a relative path inside one of the
  directories listed in ``sources``. An absolute path can also be used.

.. WARNING::

    The term ``sources_main_file`` can only be used when ``sources`` is defined. While the runtime is able to detect
    automatically the main file from application execution, this would enable to modify the automatic selection in case
    of need.

Authors section
---------------

In the **Authors** section (the whole section is optional), a single author or a list of authors can be provided. They
describe the individuals that wrote the source code of the application. For each Author:

- ``name``, ``e-mail`` and ``organisation_name`` are strings corresponding to the author's name, e-mail and their
  institution. They are free text, but the ``e-mail`` field must follow the ``user@domain.top`` format.

- ``orcid`` refers to the ORCID identifier of the author. The IDs can be found and created at https://orcid.org/

- ``ror`` refers to the Research Organization Registry (ROR) identifier for an institution.
  They can be found at http://ror.org/

.. WARNING::

    If no ``orcid`` is found online or specified for an Author, they will not be listed as such. Their corresponding
    Organization information will only be included if the Organization's ``ror`` is found online or specified directly
    in the YAML configuration file.

.. TIP::

    It is very important that the ``orcid`` and ``ror`` terms are correctly defined, since they are
    used as unique identifiers for Persons and Organizations in the RO-Crate specification. The ``orcid`` id is the
    minimum information needed to be able to add a person as an Author.

Agent section
-------------

The **Agent** section has the same terms as the Authors section, but it specifically provides the details of the sole
person running the workflow, that can be different from the Authors. The whole section is optional and only a single
individual can be provided.

.. WARNING::

    If no Agent section is provided, the first Author will be considered by default as the agent executing the
    workflow.

Automatic search of Authors and Agent
-------------------------------------

When applications have a large list of authors, having to search for all the details of each one of them can be a
tedious task. For such cases, we have implemented an automatic search of details of **Authors** and **Agent** through the
ORCID and ROR public APIs. The main requirement of this feature is that the machine from which you run the experiment
must have the possibility of opening external connections (i.e. this can be an issue at some clusters, that restrict
their outbound communications for security reasons).

The following example shows that at least the ``name`` or ``orcid`` of the person needs to be provided so the search
can be triggered and the missing pieces of information will be looked for. Any extra information provided by the user
will override the information found online, as will be shown in the following example.

.. code-block:: yaml

    COMPSs Workflow Information:
      name: COMPSs Matrix Multiplication, out-of-core using files
      description: Hypermatrix size 2x2 blocks, block size 2x2 elements
      license: CC-BY-NC-ND-4.0
      sources: [matmul_files.py, matmul_tasks.py]

    Authors:
      - name: Raül Sirvent
        e-mail: Raul.Sirvent@bsc.es
        organisation_name: Universitat Politècnica de Catalunya
      - name: Nicolò Giacomini
      - name: Fernando Vázquez Novoa
        organisation_name: Barcelona Supercomputing Center
      - name: Cristian Cătălin Tatu
      - orcid: https://orcid.org/0000-0001-5081-7244
        organisation_name: Barcelona Supercomputing Center
      - orcid: https://orcid.org/0000-0001-6401-6229
        ror: https://ror.org/05r78ng12
      - name: Francesc Lordan
        ror: https://ror.org/05sd8tv96

    Agent:
      name: Rosa M Badia
      e-mail: Rosa.M.Badia@upc.edu
      ror: https://ror.org/03mb6wj31

Analyzing the example, we can see that at least the ``name`` or the ``orcid`` is provided in all the cases. Besides,
we can complete or override any details found online. For ``Raül Sirvent``, the automatic search will return ``Barcelona
Supercomputing Center`` as organization, but since the term ``organisation_name`` is specified, it overrides the search
result with ``Universitat Politècnica de Catalunya``. For ``Francesc Lordan`` we override his organization using the ROR.
Finally, in ``Raül Sirvent`` and ``Rosa M Badia`` we complete the ``e-mail`` information, that cannot be obtained online.

The provenance generation will print in the standard output the searches, and the results of each search, as shown in
the following lines:

.. code-block:: console

    PROVENANCE | STARTING RO-CRATE GENERATION SCRIPT
    PROVENANCE | PERSON 'Raül Sirvent': Searching ORCID, Organisation and e-Mail
    PROVENANCE | Fetched data. Given name(s): Raül, Family name(s): Sirvent, ORCID: https://orcid.org/0000-0003-0606-2512, Organisation: Barcelona Supercomputing Center, e-Mail: None
    PROVENANCE | ORGANISATION 'Universitat Politècnica de Catalunya': Searching ROR and URL
    PROVENANCE | Fetched data. Organisation: Universitat Politècnica de Catalunya, ROR: https://ror.org/03mb6wj31, URL: https://www.upc.edu
    PROVENANCE | PERSON 'Nicolò Giacomini': Searching ORCID, Organisation and e-Mail
    PROVENANCE | Fetched data. Given name(s): Nicolò, Family name(s): Giacomini, ORCID: https://orcid.org/0009-0005-2797-8177, Organisation: Barcelona Supercomputing Center, e-Mail: None
    PROVENANCE | ORGANISATION 'Barcelona Supercomputing Center': Searching ROR and URL
    PROVENANCE | Fetched data. Organisation: Barcelona Supercomputing Center, ROR: https://ror.org/05sd8tv96, URL: https://www.bsc.es/
    PROVENANCE | PERSON 'Fernando Vázquez Novoa': Searching ORCID, Organisation and e-Mail
    PROVENANCE | Fetched data. Given name(s): Fernando, Family name(s): Vázquez Novoa, ORCID: https://orcid.org/0000-0001-5634-509X, Organisation: None, e-Mail: None
    PROVENANCE | ORGANISATION 'Barcelona Supercomputing Center': Searching ROR and URL
    PROVENANCE | Fetched data. Organisation: Barcelona Supercomputing Center, ROR: https://ror.org/05sd8tv96, URL: https://www.bsc.es/
    PROVENANCE | PERSON 'Cristian Cătălin Tatu': Searching ORCID, Organisation and e-Mail
    PROVENANCE | Fetched data. Given name(s): Cristian Cătălin, Family name(s): Tatu, ORCID: https://orcid.org/0009-0003-8848-9436, Organisation: Barcelona Supercomputing Center, e-Mail: None
    PROVENANCE | ORGANISATION 'Barcelona Supercomputing Center': Searching ROR and URL
    PROVENANCE | Fetched data. Organisation: Barcelona Supercomputing Center, ROR: https://ror.org/05sd8tv96, URL: https://www.bsc.es/
    PROVENANCE | PERSON 'https://orcid.org/0000-0001-5081-7244': Searching Name, Organisation and e-Mail
    PROVENANCE | Fetched data. Given name(s): Daniele, Family name(s): Lezzi, Organisation: Barcelona Global, e-Mail: None
    PROVENANCE | ORGANISATION 'Barcelona Supercomputing Center': Searching ROR and URL
    PROVENANCE | Fetched data. Organisation: Barcelona Supercomputing Center, ROR: https://ror.org/05sd8tv96, URL: https://www.bsc.es/
    PROVENANCE | PERSON 'https://orcid.org/0000-0001-6401-6229': Searching Name, Organisation and e-Mail
    PROVENANCE | Fetched data. Given name(s): Javier, Family name(s): Conejero, Organisation: Barcelona Supercomputing Center, e-Mail: francisco.conejero@bsc.es
    PROVENANCE | ORGANISATION 'https://ror.org/05r78ng12': Searching for Name and URL
    PROVENANCE | Fetched data. Organisation: University of Castilla-La Mancha, ROR: https://ror.org/05r78ng12, URL: https://www.uclm.es
    PROVENANCE | PERSON 'Francesc Lordan': Searching ORCID, Organisation and e-Mail
    PROVENANCE | Fetched data. Given name(s): Francesc, Family name(s): Lordan, ORCID: https://orcid.org/0000-0002-9845-8890, Organisation: Universitat Politècnica de Catalunya, e-Mail: francesc.lordan@bsc.es
    PROVENANCE | ORGANISATION 'https://ror.org/05sd8tv96': Searching for Name and URL
    PROVENANCE | Fetched data. Organisation: Barcelona Supercomputing Center, ROR: https://ror.org/05sd8tv96, URL: https://www.bsc.es/
    ...
    PROVENANCE | PERSON 'Rosa M Badia': Searching ORCID, Organisation and e-Mail
    PROVENANCE | Fetched data. Given name(s): Rosa M, Family name(s): Badia, ORCID: https://orcid.org/0000-0003-2941-5499, Organisation: Barcelona Supercomputing Center, e-Mail: None
    PROVENANCE | ORGANISATION 'https://ror.org/03mb6wj31': Searching for Name and URL
    PROVENANCE | Fetched data. Organisation: Universitat Politècnica de Catalunya, ROR: https://ror.org/03mb6wj31, URL: https://www.upc.edu

When the search is successful, and some update happens in any of the persons referenced (i.e. when a non-existing field
is added), a new ``GENERATED_[your_YAML].yaml`` file is produced. This newly generated file can be used in future runs
of the experiment, either to avoid searching again for all the details of the Authors and Agent, or because the
machine does not have outbound connectivity, so all details need to be added in advance. An example of an automatically
generated file follows:

.. code-block:: yaml

    Agent:
      Updated: true
      e-mail: Rosa.M.Badia@upc.edu
      familyName: Badia
      givenName: Rosa M
      name: Rosa M Badia
      orcid: https://orcid.org/0000-0003-2941-5499
      organisation_name: "Universitat Polit\xE8cnica de Catalunya"
      ror: https://ror.org/03mb6wj31
    Authors:
    - Updated: true
      e-mail: Raul.Sirvent@bsc.es
      familyName: Sirvent
      givenName: "Ra\xFCl"
      name: "Ra\xFCl Sirvent"
      orcid: https://orcid.org/0000-0003-0606-2512
      organisation_name: "Universitat Polit\xE8cnica de Catalunya"
      ror: https://ror.org/03mb6wj31
    - Updated: true
      familyName: Giacomini
      givenName: "Nicol\xF2"
      name: "Nicol\xF2 Giacomini"
      orcid: https://orcid.org/0009-0005-2797-8177
      organisation_name: Barcelona Supercomputing Center
      ror: https://ror.org/05sd8tv96
    - Updated: true
      familyName: "V\xE1zquez Novoa"
      givenName: Fernando
      name: "Fernando V\xE1zquez Novoa"
      orcid: https://orcid.org/0000-0001-5634-509X
      organisation_name: Barcelona Supercomputing Center
      ror: https://ror.org/05sd8tv96
    - Updated: true
      familyName: Tatu
      givenName: "Cristian C\u0103t\u0103lin"
      name: "Cristian C\u0103t\u0103lin Tatu"
      orcid: https://orcid.org/0009-0003-8848-9436
      organisation_name: Barcelona Supercomputing Center
      ror: https://ror.org/05sd8tv96
    - Updated: true
      familyName: Lezzi
      givenName: Daniele
      name: Daniele Lezzi
      orcid: https://orcid.org/0000-0001-5081-7244
      organisation_name: Barcelona Supercomputing Center
      ror: https://ror.org/05sd8tv96
    - Updated: true
      e-mail: francisco.conejero@bsc.es
      familyName: Conejero
      givenName: Javier
      name: Javier Conejero
      orcid: https://orcid.org/0000-0001-6401-6229
      organisation_name: University of Castilla-La Mancha
      ror: https://ror.org/05r78ng12
    - Updated: true
      e-mail: francesc.lordan@bsc.es
      familyName: Lordan
      givenName: Francesc
      name: Francesc Lordan
      orcid: https://orcid.org/0000-0002-9845-8890
      organisation_name: Barcelona Supercomputing Center
      ror: https://ror.org/05sd8tv96
    COMPSs Workflow Information:
      data_persistence: true
      description: Hypermatrix size 2x2 blocks, block size 2x2 elements
      license: CC-BY-NC-ND-4.0
      name: COMPSs Matrix Multiplication, out-of-core using files
      sources:
      - matmul_files.py
      - matmul_tasks.py

Examples
--------

In the following lines, we provide a YAML example for an out-of-core Matrix Multiplication PyCOMPSs application,
distributed with license Apache v2.0, with two source files, and authored by two persons from two different
institutions. Since no ``Agent`` is defined, the first author is considered as such by default. The ``data_persistence``
term is set to ``True``, to indicate the datasets should be included in the resulting crate.

.. code-block:: yaml

    COMPSs Workflow Information:
      name: COMPSs Matrix Multiplication, out-of-core using files
      description: Hypermatrix size 2x2 blocks, block size 2x2 elements
      license: Apache-2.0
      sources: [matmul_directory.py, matmul_tasks.py]
      data_persistence: True

    Authors:
      - name: Raül Sirvent
        e-mail: Raul.Sirvent@bsc.es
        orcid: https://orcid.org/0000-0003-0606-2512
        organisation_name: Barcelona Supercomputing Center
        ror: https://ror.org/05sd8tv96
      - name: Rosa M. Badia
        e-mail: Rosa.M.Badia@upc.edu
        orcid: https://orcid.org/0000-0003-2941-5499
        organisation_name: Universitat Politècnica de Catalunya
        ror: https://ror.org/03mb6wj31

Also, another example of a COMPSs Java K-means application, where the usage of ``sources`` including directories can be seen.
We add to the crate the sub-directories that contain the ``.jar`` and ``.java`` files. In this case,
an ``Agent`` is provided which is different from the person that wrote the application. The term ``data_persistence``
has been explicitly specified, but since the default value is ``False`` if not specified, it could be removed and still
obtain the same result. Finally, the ``trace_persistence`` term is set to True, indicating that, if traces are generated
when running this experiment, they will be included in the crate.

.. code-block:: yaml

    COMPSs Workflow Information:
      name: COMPSs K-means
      description: K-means clustering is a method of cluster analysis that aims to partition ''n'' points into ''k''
        clusters in which each point belongs to the cluster with the nearest mean. It follows an iterative refinement
        strategy to find the centers of natural clusters in the data.
      license: https://opensource.org/licenses/Apache-2.0
      sources: [jar/, src/]
      data_persistence: False
      trace_persistence: True

    Authors:
      name: Raül Sirvent
      e-mail: Raul.Sirvent@bsc.es
      orcid: https://orcid.org/0000-0003-0606-2512
      organisation_name: Barcelona Supercomputing Center
      ror: https://ror.org/05sd8tv96

    Agent:
      name: Rosa M. Badia
      e-mail: Rosa.M.Badia@upc.edu
      orcid: https://orcid.org/0000-0003-2941-5499
      organisation_name: Universitat Politècnica de Catalunya
      ror: https://ror.org/03mb6wj31

An example of the **minimal YAML** that needs to be defined in order to publish your workflow in WorkflowHub is:

.. code-block:: yaml

    COMPSs Workflow Information:
      name: COMPSs K-means

.. TIP::

    While effectively the only mandatory field to be able to publish a workflow in WorkflowHub is ``name`` inside the **COMPSs
    Workflow Information** section, we encourage application owners to include all the fields detailed in the YAML in
    order to get all the benefits of recording workflow provenance. For instance, if no authors are included, it will
    not be possible to generate a DOI for the workflow.
