Task Selection
==============

As in the case of Python, a COMPSs R application is a R
sequential program that contains calls to tasks. In particular, the user
can select as a task R functions.

The task definition in R is done by means of R decorators (or function wrappers)
instead of an annotated interface. In particular, the user needs to add
a ``task`` decorator that describes the task before the
definition of the function.

As an example (:numref:`code_r`), let us assume that the application calls
a function **add**, which receives two integer parameters (``x`` and ``y``).
The code of **add** adds the value of ``x`` and ``y``.

.. code-block:: r
    :name: code_r
    :caption: R application example

    def foo(file_path, value):
        """ Update the file 'file_path' with the 'value'"""
        with open(file_path, "a") as fd:
            fd.write(value)

    def main():
        my_file = "sample_file.txt"
        with open(my_file, "w") as fd:
            fd.write("Hello")
        foo(my_file, "World")

    if __name__ == '__main__':
        main()


.. code-block:: r
    :name: code_r_task
    :caption: R application example function file (``add.R``)

    add <- function(x, y) {
        return(x + y)
    }


.. code-block:: r
    :name: code_r_main
    :caption: R application example main file (``addition.R``)

    source("add.R")

    add.t <- task(add, "add.R", return_value = TRUE)
    a <- 2; b <- 3;
    result <- add.t(a, b)
    cat("The result is:", result, "\n")


In order to select **add** as a task, the corresponding ``task``
decorator needs to be placed wrapping the definition of the
function, providing some metadata about the parameters of that function.
The ``task`` decorator has to be imported from the *RCOMPS*
library (:numref:`task_import_r`).

.. code-block:: r
    :name: task_import_r
    :caption: R task import and definition

    library(RCOMPSs)
    source("add.R")
    compss_start()

    add.t <- task(add, "add.R", return_value = TRUE)
    ...

    compss_stop()


.. dropdown:: See complete example

    .. code-block:: r
        :name: code_r_task_complete
        :caption: R application example function file (``add.R``)

        add <- function(x, y) {
            return(x + y)
        }


    .. code-block:: r
        :name: code_r_main_complete
        :caption: R application example main file (``addition.R``)

        library(RCOMPSs)
        source("add.R")
        compss_start()

        add.t <- task(add, "add.R", return_value = TRUE)

        a <- 2; b <- 3;
        result <- add.t(a, b)
        result <- compss_wait_on(result)
        cat("The result is:", result, "\n")

        compss_stop()


.. IMPORTANT::

    It is required to invoke the ``compss_start`` and ``compss_stop``
    functions at the beginning and ending of the application to
    initialize the R binding.


.. toctree::
    :maxdepth: 4
    :caption: Table of Contents

    01_Task_selection/02_Task_parameters
    01_Task_selection/03_Other_task_parameters
    01_Task_selection/04_Task_parameters_summary
    01_Task_selection/05_Task_return
