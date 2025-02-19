===============
What is COMPSs?
===============

**COMP Superscalar (COMPSs)** is a **task-based programming model** which aims
to ease the development of applications **for distributed infrastructures**,
such as large High-Performance clusters (HPC), clouds and container managed
clusters.
COMPSs  provides a **programming interface for** the development of the
**applications** **and a runtime system that exploits the inherent parallelism**
of applications **at execution time**.

To improve programming productivity, the **COMPSs programming model** has
following **characteristics**:

- **Sequential programming:** COMPSs programmers do not need to deal with the
  typical duties of parallelization and distribution, such as thread creation
  and synchronization, data distribution, messaging or fault tolerance.
  Instead, the model is based on sequential programming, which makes it
  appealing to users that either lack parallel programming expertise or are
  looking for better programmability.

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

PyCOMPSs/COMPSs can be seen as a **programming environment for the development
of complex workflows**. For example, in the case of PyCOMPSs, while the
task-orchestration code needs to be written in Python, it supports different
types of tasks, such as Python methods, external binaries, multi-threaded
(internally parallelized with alternative programming models such as OpenMP
or pthreads), or multi-node (MPI applications).
Thanks to the use of Python as programming language, PyCOMPSs naturally
integrates well with data analytics and machine learning libraries, most of
them offering a Python interface.
PyCOMPSs also supports reading/writing streamed data.

At a lower level, the COMPSs runtime manages the execution of the workflow
components implemented with the PyCOMPSs programming model.
At runtime, it generates a **task-dependency graph** by analyzing the existing
data dependencies between the tasks defined in the Python code.
The task-graph **encodes the existing parallelism of the workflow**, which is
then scheduled and executed by the COMPSs runtime in the computing resources.

The COMPSs runtime is also able to **react to tasks failures and to exceptions**
in order to adapt the behavior accordingly.
These functionalities, offer the possibility of designing a **new category of
workflows with very dynamic behavior**, that can change their configuration
at execution time upon the occurrence of given events.

-----------------
More information:
-----------------

- Project website: http://compss.bsc.es

- Project repository: https://github.com/bsc-wdc/compss
