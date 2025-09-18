@task
=====

The task definition is the main parallelization mechanism for COMPSs.

It allows COMPSs to detect the units of work and their inputs/outputs in order to manage the execution in distributed environments.

.. TIP:: These are the main questions that will direct you to the appropriate Section

    .. grid:: 2
        :gutter: 2

        .. grid-item-card::
            :columns: 1

            :material-twotone:`looks_one;2em`

        .. grid-item-card::
            :columns: 11

            :material-twotone:`rocket_launch` :ref:`How to define a task? <Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/01_Task_decorator:Task Selection>`

        .. grid-item-card::
            :columns: 1

            :material-twotone:`looks_two;2em`

        .. grid-item-card::
            :columns: 4

            :material-twotone:`star` :ref:`How to deal with the function parameters in the task definition? <Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/01_Task_decorator:Task Parameters>`

        .. grid-item-card::
            :columns: 4

            :material-twotone:`keyboard_return` :ref:`How to deal with task return? <Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/01_Task_decorator:Task Return>`

        .. grid-item-card::
            :columns: 3

            :material-twotone:`settings` :ref:`Which are the task specific parameters? <Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/01_Task_decorator:Other Task Parameters>`

        .. grid-item-card::
            :columns: 1

            :material-twotone:`looks_3;2em`

        .. grid-item-card::
            :columns: 4

            :material-twotone:`fast_forward` :ref:`Which are all the supported function parameters types? <Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/01_Task_decorator:Task Parameters Summary>`

        .. grid-item-card::
            :columns: 4

            :material-twotone:`fast_forward` :ref:`Where can I find all supported task decorator parameters? <Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/01_Task_decorator:Task Parameters Summary>`

        .. grid-item::
            :columns: 3

        .. grid-item-card::
            :columns: 1

            :material-twotone:`looks_4;2em`

        .. grid-item-card::
            :columns: 4

            :material-twotone:`speed` :ref:`How to compile a task? <Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/01_Task_decorator:Integration with Numba>`

        .. grid-item-card::
            :columns: 4

            :material-twotone:`memory` :ref:`How to define a GPU task? <Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/01_Task_decorator:Using Numba with GPUs>`

        .. grid-item::
            :columns: 3



.. include:: ./01_Task_decorator/01_Task_selection_inc.rst

.. include:: ./01_Task_decorator/02_Task_parameters_inc.rst

.. include:: ./01_Task_decorator/03_Other_task_parameters_inc.rst

.. include:: ./01_Task_decorator/04_Task_parameters_summary_inc.rst

.. include:: ./01_Task_decorator/05_Task_return_inc.rst

.. include:: ./01_Task_decorator/06_Numba_integration_inc.rst
