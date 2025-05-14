Task Parameters Summary
~~~~~~~~~~~~~~~~~~~~~~~

:numref:``task_arguments_r`` summarizes all arguments that can be found in the *task* decorator.

.. table:: Arguments of the *task* decorator
    :name: task_arguments_r

    +---------------------+------------------------------------------------------------------------------------------------------------------------+
    | Argument            | Value                                                                                                                  |
    +=====================+=======================+================================================================================================+
    | Formal parameter    | **(default: empty)**  | The parameter is an object or a simple tipe that will be inferred.                             |
    | name                +-----------------------+------------------------------------------------------------------------------------------------+
    |                     | IN                    | Read-only parameter, all types.                                                                |
    |                     +-----------------------+------------------------------------------------------------------------------------------------+
    |                     | INOUT                 | Read-write parameter, all types except file and primitives.                                    |
    |                     +-----------------------+------------------------------------------------------------------------------------------------+
    |                     | OUT                   | Write-only parameter, all types except file and primitives (requires default constructor).     |
    +---------------------+------------------------------------------------------------------------------------------------------------------------+
    | returns             | Return type or number of returned elements                                                                             |
    +---------------------+------------------------------------------------------------------------------------------------------------------------+
