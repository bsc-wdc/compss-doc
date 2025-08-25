Decorators
**********

The programming model for Python is structured in the following sections:


.. grid::
    :gutter: 2
    :margin: 0 0 0 0
    :padding: 0 0 0 0

    .. grid-item::
        :columns: 12
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :child-direction: row

        .. grid::
            :margin: 0 0 0 0
            :padding: 0 0 0 0

            .. grid-item::
                :columns: 1

                Extra task definition

            .. grid-item::
                :columns: 1

                | **Optional**
                | (Requires :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/03_Constraint_decorator:@constraint`)

            .. grid-item::
                :columns: 6

                .. grid:: 3
                    :gutter: 2

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/19_Multiple_task_implementations:@implements`

            .. grid-item::
                :columns: 2

            .. grid-item::
                :columns: 2

    .. grid-item::
        :columns: 12
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :child-direction: row

        .. grid::
            :margin: 0 0 0 0
            :padding: 0 0 0 0

            .. grid-item::
                :columns: 1

                Fault tolerance action

            .. grid-item::
                :columns: 1

                **Optional**

            .. grid-item::
                :columns: 6

                .. grid:: 3
                    :gutter: 2

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/18_Failures_and_exceptions:@on_failure`

            .. grid-item::
                :columns: 2

            .. grid-item::
                :columns: 2

    .. grid-item::
        :columns: 12
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :child-direction: row

        .. grid::
            :margin: 0 0 0 0
            :padding: 0 0 0 0

            .. grid-item::
                :columns: 1

                | Task wrap
                | actions

            .. grid-item::
                :columns: 1

                | **Optional**
                | (One or both - Once or more)

            .. grid-item::
                :columns: 6

                .. grid:: 3
                    :gutter: 2

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/16_Prolog_decorator:@prolog`

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/17_Epilog_decorator:@epilog`

            .. grid-item::
                :columns: 2

            .. grid-item::
                :columns: 2

    .. grid-item::
        :columns: 12
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :child-direction: row

        .. grid::
            :margin: 0 0 0 0
            :padding: 0 0 0 0

            .. grid-item::
                :columns: 1

                Scheduling requirements

            .. grid-item::
                :columns: 1

                **Optional**

            .. grid-item::
                :columns: 6

                .. grid:: 3
                    :gutter: 2

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/15_IO_decorator:@IO`

            .. grid-item::
                :columns: 2

            .. grid-item::
                :columns: 2

    .. grid-item::
        :columns: 12
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :child-direction: row

        .. grid::
            :margin: 0 0 0 0
            :padding: 0 0 0 0

            .. grid-item::
                :columns: 1

                Task requirements

            .. grid-item::
                :columns: 1

                | **Optional**
                | (One or both)

            .. grid-item::
                :columns: 6

                .. grid:: 3
                    :gutter: 2

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/03_Constraint_decorator:@constraint`

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/09_Multinode_decorator:@multinode`

            .. grid-item::
                :columns: 2

            .. grid-item::
                :columns: 2

    .. grid-item::
        :columns: 12
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :child-direction: row

        .. grid::
            :margin: 0 0 0 0
            :padding: 0 0 0 0

            .. grid-item::
                :columns: 1

                Type of task

            .. grid-item::
                :columns: 1

                | **Optional**
                | (Only one)

            .. grid-item::
                :columns: 6

                .. grid:: 3
                    :gutter: 2

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/04_Binary_decorator:@binary`

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/05_OmpSs_decorator:@ompss`

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/06_MPI_decorator:@mpi`

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/07_MPMD_MPI_decorator:@mpmd_mpi`

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/08_COMPSs_decorator:@compss`

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/10_HTTP_decorator:@http`

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/11_Reduction_decorator:@reduction`

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/12_Container_decorator:@container`

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/13_Julia_decorator:@julia`

            .. grid-item::
                :columns: 2

            .. grid-item::
                :columns: 2

    .. grid-item::
        :columns: 12
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :child-direction: row

        .. grid::
            :margin: 0 0 0 0
            :padding: 0 0 0 0

            .. grid-item::
                :columns: 1

                Parameter modifiers

            .. grid-item::
                :columns: 1

                | **Optional**
                | (Once or more)

            .. grid-item::
                :columns: 6

                .. grid:: 3
                    :gutter: 2

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/14_Data_Transformation_decorator:@dt`

            .. grid-item::
                :columns: 2

                .. grid:: 1
                    :gutter: 2

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/14_Data_Transformation_decorator:@dt`

            .. grid-item::
                :columns: 2

    .. grid-item::
        :columns: 12
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :child-direction: row

        .. grid::
            :margin: 0 0 0 0
            :padding: 0 0 0 0

            .. grid-item::
                :columns: 1

                Task definition

            .. grid-item::
                :columns: 1

                | **Mandatory**
                | (Only one)

            .. grid-item::
                :columns: 6

                .. grid:: 1
                    :gutter: 2

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/01_Task_decorator:@task`

            .. grid-item::
                :columns: 2

                .. grid:: 1
                    :gutter: 2

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/02_Software_decorator:@software`

            .. grid-item::
                :columns: 2

                .. grid:: 1
                    :gutter: 2

                    .. grid-item-card::

                        :ref:`Sections/02_App_Development/02_Python/01_Programming_model/01_Decorators/20_Local_decorator:@local`




.. toctree::
    :hidden:
    :maxdepth: 4
    :caption: Table of Contents

    01_Decorators/01_Task_decorator
    01_Decorators/02_Software_decorator
    01_Decorators/03_Constraint_decorator
    01_Decorators/04_Binary_decorator
    01_Decorators/05_OmpSs_decorator
    01_Decorators/06_MPI_decorator
    01_Decorators/07_MPMD_MPI_decorator
    01_Decorators/08_COMPSs_decorator
    01_Decorators/09_Multinode_decorator
    01_Decorators/10_HTTP_decorator
    01_Decorators/11_Reduction_decorator
    01_Decorators/12_Container_decorator
    01_Decorators/13_Julia_decorator
    01_Decorators/14_Data_Transformation_decorator
    01_Decorators/15_IO_decorator
    01_Decorators/16_Prolog_decorator
    01_Decorators/17_Epilog_decorator
    01_Decorators/18_Failures_and_exceptions
    01_Decorators/19_Multiple_task_implementations
    01_Decorators/20_Local_decorator
    01_Decorators/XX_Other_task_types
