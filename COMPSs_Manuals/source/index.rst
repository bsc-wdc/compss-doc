.. COMPSs documentation master file, created by
   sphinx-quickstart on Thu Oct  3 13:27:53 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:gitlab_url: http://compss.bsc.es/gitlab/documents/documentation/tree/rtd-documentation/COMPSs_Manuals/rtd

Welcome to COMPSs!
==================

.. figure:: /Logos/COMPSs_logo.png
   :width: 30.0%
   :align: center
   :target: http://compss.bsc.es

**COMP Superscalar (COMPSs)** is a **task-based programming model** which aims
to ease the development of applications **for distributed infrastructures**,
such as large High-Performance clusters (HPC), clouds and container managed
clusters.
COMPSs  provides a **programming interface for** the development of the
**applications** **and a runtime system that exploits the inherent parallelism**
of applications **at execution time**.

To improve programming productivity, the **COMPSs programming model** has
following **characteristics**:

- **Agnostic of the actual computing infrastructure:** COMPSs offers a model
  that abstracts the application from the underlying distributed infrastructure.
  Hence, COMPSs programs do not include any detail that could tie them to a
  particular platform, like deployment or resource management.
  This makes applications portable between infrastructures with diverse
  characteristics.

- **Single memory and storage space:** the memory and file system space is also
  abstracted in COMPSs, giving the illusion that a single memory space and single
  file system is available. The runtime takes care of all the necessary data
  transfers.

- **Standard programming languages:** COMPSs is based on the popular programming
  language Java, but also offers language bindings for Python (PyCOMPSs) and
  C/C++ applications.
  This makes it easier to learn the model since programmers can reuse most of
  their previous knowledge.

- **No APIs:** In the case of COMPSs applications in Java, the model does not
  require to use any special API call, pragma or construct in the application;
  everything is pure standard Java syntax and libraries.
  With regard the Python and C/C++ bindings, a small set of API calls should
  be used on the COMPSs applications.


This manual is divided in 12 sections:

.. toctree::
   :maxdepth: 1

   Sections/0_Intro
   Sections/00_Quickstart
   Sections/01_Installation
   Sections/02_App_Development
   Sections/03_Execution_Environments
   Sections/05_Tools
   Sections/06_Persistent_Storage
   Sections/07_Sample_Applications
   Sections/08_PyCOMPSs_CLI
   Sections/09_PyCOMPSs_Notebooks
   Sections/04_Troubleshooting
   Sections/10_Tutorial


.. Indices and tables
   ==================
   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
