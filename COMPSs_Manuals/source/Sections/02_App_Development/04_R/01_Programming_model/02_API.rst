.. spelling:word-list::

    rw

API
===

RCOMPSs provides an API for data synchronization and barrier.

Synchronization
---------------

The main program of the application is a sequential code that contains
calls to the selected tasks. In addition, when synchronizing for task
data from the main program, there exist six API functions that can be invoked:

compss_barrier(no_more_tasks=False)
   Performs a explicit synchronization, but does not return any object.
   The use of *compss_barrier()* forces to wait for all tasks that have been
   submitted before the *compss_barrier()* is called. When all tasks
   submitted before the *compss_barrier()* have finished, the execution
   continues. The *no_more_tasks* is used to specify if no more tasks
   are going to be submitted after the *compss_barrier()*.

compss_wait_on(obj)
   Synchronizes for the last version of object specified by *obj* and returns
   the synchronized object.

To illustrate the use of the aforementioned API functions, the following
example (:numref:`api_usage_r`).

.. code-block:: r
    :name: api_usage_r
    :caption: RCOMPSs Synchronization API functions usage

    library(RCOMPSs)
    source("file_with_functions.R")
    compss_start()

    add.t <- task(add, "add.R", return_value = TRUE)

    a <- 1; b <- 2;
    result <- add.t(a, b)

    compss_barrier()

    ...

    result <- compss_wait_on(result)

    cat("The result is:", result, "\n")
    compss_stop()


API Summary
-----------

Finally, :numref:`r_api_functions` summarizes the API functions to be
used in the main program of a COMPSs R application.

.. table:: COMPSs R API functions
    :name: r_api_functions

    +-----------------+----------------------------------------------+-----------------------------------------------------------------------------------------+
    | Type            | API Function                                 | Description                                                                             |
    +=================+==============================================+=========================================================================================+
    | Synchronization | compss_barrier()                             | Wait for all tasks submitted before the barrier.                                        |
    |                 +----------------------------------------------+-----------------------------------------------------------------------------------------+
    |                 | compss_wait_on(obj)                          | Synchronizes for the last version of an object and returns it.                          |
    +-----------------+----------------------------------------------+-----------------------------------------------------------------------------------------+
