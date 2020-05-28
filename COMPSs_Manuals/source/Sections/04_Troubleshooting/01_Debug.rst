How to debug
============

When an error/exception happens during the execution of an application, the
first thing that users must do is to check the application output:

- Using ``runcompss`` the output is shown in the console.

- Using ``enqueue_compss`` the output is in the ``compss-<JOB_ID>.out`` and
  ``compss-<JOB_ID>.err``

If the error happens within a task, it will not appear in these files.
Users must check the log folder in order to find what has failed.
The log folder is by default in:

- Using ``runcompss``: ``$HOME/.COMPSs/<APP_NAME>_XX`` (where XX is a number
  between 00 and 99, and increases on each run).

- Using ``enqueue_compss``: ``$HOME/.COMPSs/<JOB_ID>``

This log folder contains the ``jobs`` folder, where all output/errors of the
tasks are stored. In particular, each task produces a ``JOB<TASK_NUMBER>_NEW.out``
and ``JOB<TASK_NUMBER>_NEW.err`` files when a task fails.

.. TIP::

    If the user enables the **debug mode** by including the ``-t`` flag into
    ``runcompss`` or ``enqueue_compss`` command, more information will be
    stored in the log folder of each run easing the error detection.
    In particular, all output and error output of all tasks will appear
    within the ``jobs`` folder.

    In addition, some more log files will appear:

    -  ``runtime.log``

    -  ``pycompss.log`` (only if using the Python binding).

    -  ``pycompss.err`` (only if using the Python binding and an error in the
       binding happens.)

    -  ``resources.log``

    -  ``workers`` folder. This folder will contain four files per worker node:

        - ``worker_<MACHINE_NAME>.out``

        - ``worker_<MACHINE_NAME>.err``

        - ``binding_worker_<MACHINE_NAME>.out``

        - ``binding_worker_<MACHINE_NAME>.err``

    As a suggestion, users should check the last lines of the ``runtime.log``.
    If the file-transfers or the tasks are failing an error message will appear
    in this file. If the file-transfers are successfully and the jobs are
    submitted, users should check the ``jobs`` folder and look at the error
    messages produced inside each job. Users should notice that if there are
    **RESUBMITTED** files something inside the job is failing.

    If the ``workers`` folder is empty, means that the execution failed and
    the COMPSs runtime was not able to retrieve the workers logs. In this case,
    users must connect to the workers and look directly into the worker logs.
    Alternatively, if the user is running with a shared disk (e.g. in a
    supercomputer), the user can define a shared folder in the
    ``--worker_working_directory=/shared/folder`` where a ``tmp_XXXXXX`` folder
    will be created on the application execution and all worker logs will be
    stored.


The following subsections show debugging examples depending on the choosen
flavour (Java, Python or C/C++).

.. toctree::
    :maxdepth: 2
    :caption: Debugging examples

    01_Debugging_examples/01_Java
    01_Debugging_examples/02_Python
    01_Debugging_examples/03_C
