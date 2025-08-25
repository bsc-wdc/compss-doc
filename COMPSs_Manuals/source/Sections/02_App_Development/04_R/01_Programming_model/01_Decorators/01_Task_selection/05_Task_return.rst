Task Return
===========

If the function or method returns a value, the programmer can use the
*returns* argument within the *task* decorator. In this
argument, the programmer can specify the type of that value
(:numref:`task_returns_r`).


.. code-block:: r
    :name: code_r_task_complete_returns
    :caption: R application example function file (``add.R``)

    add <- function(x, y) {
        return(x + y)
    }


.. code-block:: r
    :name: task_returns_r
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
