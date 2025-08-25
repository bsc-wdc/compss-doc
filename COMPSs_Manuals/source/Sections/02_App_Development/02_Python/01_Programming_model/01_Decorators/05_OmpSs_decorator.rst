@ompss
======

The *@ompss* (or @OmpSs) decorator shall be used to define that a task is
going to invoke a OmpSs executable (:numref:`ompss_task_python`).

Definition
----------

.. code-block:: python
    :name: ompss_task_python
    :caption: OmpSs task example

    from pycompss.api.ompss import ompss

    @ompss(binary="ompssApp.bin")
    @task()
    def ompss_func():
         pass

The OmpSs executable invocation can also be enriched with parameters,
files and prefixes as with the *@binary* decorator through the
function parameters and *@task* decorator information. Please,
check :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/04_Binary_decorator:@binary` for more details.
