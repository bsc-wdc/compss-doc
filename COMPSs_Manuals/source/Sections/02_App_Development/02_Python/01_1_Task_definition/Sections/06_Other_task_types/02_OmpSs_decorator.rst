OmpSs decorator
^^^^^^^^^^^^^^^

The *@ompss* (or @OmpSs) decorator shall be used to define that a task is
going to invoke a OmpSs executable (:numref:`ompss_task_python`).

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
check :ref:`sections/02_app_development/02_python/01_1_task_definition/sections/06_Other_task_types/01_Binary_decorator:Binary decorator` for more details.
