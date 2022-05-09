Integration with Numba
----------------------

PyCOMPSs can also be used with Numba. Numba (http://numba.pydata.org/)
is an Open Source JIT compiler for Python which provides a set of
decorators and functionalities to translate Python functions to optimized
machine code.

Basic usage
~~~~~~~~~~~

PyCOMPSs’ tasks can be decorated with Numba’s ``@jit``/\ ``@njit`` decorator
(with the appropiate parameters) just below the @task decorator in order to
apply Numba to the task.

.. code-block:: python

    from pycompss.api.task import task     # Import @task decorator
    from numba import jit

    @task(returns=1)
    @jit()
    def numba_func(a, b):
         ...

The task will be optimized by Numba within the worker node, enabling COMPSs
to use the most efficient implementation of the task (and exploiting the
compilation cache -- any task that has already been compiled does not need
to be recompiled in subsequent invocations).

Advanced usage
~~~~~~~~~~~~~~

PyCOMPSs can be also used in conjuntion with the Numba’s
``@vectorize``, ``@guvectorize``, ``@stencil`` and ``@cfunc``.
But since these decorators do not preserve the original argument specification
of the original function, their usage is done through the *numba* parameter
withih the ``@task`` decorator.
The *numba* parameter accepts:

- **Boolean**:
    ``True``: Applies *jit* to the function.

- **Dictionary{k, v}**:
    Applies *jit* with the dictionary parameters to the function
    (allows to specify specific jit parameters (e.g. ``nopython=True``)).

- **String**:
    - ``"jit"``: Applies *jit* to the function.
    - ``"njit"``: Applies *jit* with *nopython=True* to the function.
    - ``"generated_jit"``: Applies *generated_jit* to the function.
    - ``"vectorize"``: Applies *vectorize* to the function. Needs some extra flags in the *@task* decorator:

      - *numba_signature*: String with the *vectorize* signature.

    - ``"guvectorize"``: Applies *guvectorize* to the function. Needs some extra flags in the *@task* decorator:

      - *numba_signature*: String with the *guvectorize* signature.
      - *numba_declaration*: String with the *guvectorize* declaration.

    - ``"stencil"``: Applies *stencil* to the function.
    - ``"cfunc"``: Applies   *cfunc* to the function. Needs some extra flags in the *@task* decorator:

      - *numba_signature*: String with the *cfunc* signature.

Moreover, the *@task* decorator also allows to define specific flags for the
*jit*, *njit*, *generated_jit*, *vectorize*, *guvectorize* and *cfunc*
functionalities with the *numba_flags* hint.
This hint is used to declare a dictionary with the flags expected to use
with these numba functionalities. The default flag included by PyCOMPSs
is the ``cache=True`` in order to exploit the function caching of Numba
across tasks.

For example, to apply Numba *jit* to a task:

.. code-block:: python

    from pycompss.api.task import task

    @task(numba='jit')  # Aternatively: @task(numba=True)
    def jit_func(a, b):
         ...

And if the developer wants to use specific flags with *jit* (e.g.
``parallel=True``), the *numba_flags* must be defined with a dictionary where
the key is the numba flag name, and the value, the numba flag value to use):

.. code-block:: python

    from pycompss.api.task import task

    @task(numba='jit', numba_flags={'parallel':True})
    def jit_func(a, b):
         ...

Other Numba’s functionalities require the specification of the function
signature and declaration. In the next example a task that will use the
*vectorize* with three parameters and a specific flag to target the CPU
is shown:

.. code-block:: python

    from pycompss.api.task import task

    @task(returns=1,
          numba='vectorize',
          numba_signature=['float32(float32, float32, float32)'],
          numba_flags={'target':'cpu'})
    def vectorize_task(a, b, c):
        return a * b * c


Using Numba with GPUs
^^^^^^^^^^^^^^^^^^^^^

In addition, Numba is also able to optimize python code for GPUs that can be
used within PyCOMPSs' tasks. :ref:`numba_gpus` shows an example where the
``calculate_wight`` task has a constraint of one CPU and one GPU. This task
first transfers the necessary data to the GPU using Numba's ``cuda`` module,
then invokes the ``calculate_weight_cuda`` function (that is decorated with
the Numba's ``@vectorize`` decorator defining its signature and the target
specifically for GPU). When the execution in the GPU of the
``calculate_weight_cuda`` finishes, the result is transfered to the cpu with
the ``copy_to_host`` function and the task result is returned.


.. code-block:: python
    :name: numba_gpus
    :caption: Task using Numba and a GPU

    from pycompss.api.constraint import constraint
    from pycompss.api.task import task
    from pycompss.api.parameter import *
    from numba import vectorize
    from numba import cuda

    @constraint(processors=[{'ProcessorType':'CPU', 'ComputingUnits':'1'},
                            {'ProcessorType':'GPU', 'ComputingUnits':'1'}])
    @task(returns=1)
    def calculate_weight(min_depth, max_depth, e3t, depth, mask):
        # Transfer data to the GPU
        gpu_mask = cuda.to_device(mask.data.astype(np.float32))
        gpu_e3t = cuda.to_device(e3t.data.astype(np.float32))
        gpu_depth = cuda.to_device(depth.data.astype(np.float32))
        # Invoke function compiled with Numba for GPU
        weight = calculate_weight_cuda(min_depth, max_depth,
                                       gpu_e3t, gpu_depth, gpu_mask)
        # Tranfer result from GPU
        local_weight = weight.copy_to_host()
        return local_weight

    @vectorize(['float32(int32, int32, float32, float32, float32)'], target='cuda')
    def calculate_weight_cuda(min_depth, max_depth, e3t, depth, mask):
        """
        This code is compiled with Numba for GPU (cuda)
        """
        if not mask:
            return 0
        top = depth
        bottom = top + e3t
        if bottom < min_depth or top > max_depth:
            return 0
        else:
            if top < min_depth:
                top = min_depth
            if bottom > max_depth:
                bottom = max_depth

            return (bottom - top) * 1020 * 4000

.. CAUTION::

    The function compiled with Numba for GPU can not be a task since the
    step to transfer the data to the GPU and backwards needs to be explicitly
    performed by the user.

    For this reason, the appropiate structure is composed by a task that
    has the necessary constraints, deals with the data movements and invokes
    the function compiled with Numba for GPU.

    The main application can then invoke the task.


.. IMPORTANT::

    In order to run with GPUs in local machine, you need to define the available
    GPUs in the ``project.xml`` file.

    As example, the following ``project.xml`` and ``resources.xml`` shall be
    used with the ``--project`` and ``--resources`` correspondingly:

    * :download:`project.xml <Resources/project.xml>`
    * :download:`resources.xml <Resources/resources.xml>`


More details about Numba and the specification of the signature, declaration
and flags can be found in the Numba’s webpage
(http://numba.pydata.org/).
