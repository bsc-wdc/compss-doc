.. spelling:word-list::

   ab
   cd
   ef
   gh
   abcd
   efgh


Addition
********

The Addition application is a R application that performs several additions
by means of a task. The initial values are 8 and they are accumulated
two by two. Next, we provide the main code and the task declaration:

.. code-block:: r
      :caption: ``add.R``

      add <- function(x, y) {
         return(x + y)
      }


.. code-block:: r
      :caption: ``addition.R``

      library(RCOMPSs)
      source("add.R")
      compss_start()

      add.t <- task(add, "add.R", info_only = FALSE, return_value = TRUE)

      a <- 2; b <- 3;
      c <- 4; d <- 5;
      e <- 6; f <- 7;
      g <- 8; h <- 9;

      # Task (1) a + b
      ab <- add.t(a, b)
      # Task (2) c + d
      cd <- add.t(c, d)
      # Task (3) e + f
      ef <- add.t(e, f)
      # Task (4) g + h
      gh <- add.t(g, h)

      # Task (5) ab + cd
      abcd <- add.t(ab, cd)
      # Task (6) ef + gh
      efgh <- add.t(ef, gh)

      # Task (7) abcd + efgh
      result <- add.t(abcd, efgh)

      # Retrieve the result
      result <- compss_wait_on(result)
      cat("The result is:", result, "\n")

      compss_stop()


This code uses the ``add`` function described in the ``add.R`` file to add:
  - ``a`` and ``b`` into ``ab``
  - ``c`` and ``d`` into ``cd``
  - ``e`` and ``f`` into ``ef``
  - ``g`` and ``h`` into ``gh``
Then adds these partial results:
  - ``ab`` and ``cd`` into ``abcd``
  - ``ef`` and ``gh`` into ``efgh``
And finally adds these partial results to achieve the final result:
  - ``abcd`` and ``efgh`` into ``result``

On a normal R execution, each addition will be done after the other
(sequentially), accumulating the computational time.
RCOMPSs is able to parallelize this code thanks to its ``task``
decorator which wraps the ``add`` function instantiating the
``add.t`` function, and synchronize the results with the
``compss_wait_on`` API call.

The Addition application can be executed by invoking the ``runcompss`` command
with the application file name and the ``--lang=r`` flag.

The following lines provide an example of its execution.

.. code-block:: console

    $ runcompss --lang=r addition.R
      [  INFO] Inferred PYTHON language
      [  INFO] Using default location for project file: /opt/COMPSs/Runtime/configuration/xml/projects/default_project.xml
      [  INFO] Using default location for resources file: /opt/COMPSs/Runtime/configuration/xml/resources/default_resources.xml
      [  INFO] Using default execution type: compss

      ----------------- Executing addition.R --------------------------

      WARNING: COMPSs Properties file is null. Setting default values
      [(763)    API]  -  Starting COMPSs Runtime v3.3.3.post2505 (build 20250513-0839.rfcc8f551ada00b095448810eee6b34a1baca40f8)
      The result is: 44
      [(9528)    API]  -  Execution Finished

      ------------------------------------------------------------


The task dependency graph is depicted in the next figure.
It shows the parallelism that COMPSs has extracted and taken advantage of.

.. figure:: /Sections/00_Quickstart/Figures/addition.png
     :alt: The dependency graph of the addition application
     :align: center
     :width: 30.0%

     The dependency graph of the addition application

COMPSs has detected that the addition of ``a+b`` and ``c+d`` is independent,
and consequently, that they can be done in parallel. While the addition
of ``res1+res2`` waits for the previous additions.
