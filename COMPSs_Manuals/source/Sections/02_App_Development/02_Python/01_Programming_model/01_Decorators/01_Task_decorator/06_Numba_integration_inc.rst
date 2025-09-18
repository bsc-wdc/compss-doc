Integration with Numba
----------------------

PyCOMPSs can also be used with Numba. Numba (http://numba.pydata.org/)
is an Open Source JIT compiler for Python which provides a set of
decorators and functionalities to translate Python functions to optimized
machine code.

Basic usage
^^^^^^^^^^^

PyCOMPSs' tasks can be decorated with Numba's ``@jit``/\ ``@njit`` decorator
(with the appropriate parameters) just below the @task decorator in order to
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
^^^^^^^^^^^^^^

PyCOMPSs can be also used in conjunction with the Numba's
``@vectorize``, ``@guvectorize``, ``@stencil`` and ``@cfunc``.
But since these decorators do not preserve the original argument specification
of the original function, their usage is done through the *numba* parameter
within the ``@task`` decorator.
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

Other Numba's functionalities require the specification of the function
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
"""""""""""""""""""""

In addition, Numba is also able to optimize python code for GPUs that can be
used within PyCOMPSs' tasks. :ref:`numba_gpus` shows an example of a task
that performs a matrix multiplication in GPU (code from
`Numba documentation <https://numba.pydata.org/numba-doc/dev/cuda/examples.html>`_).

The ``main`` function creates the input and output matrices, and invokes
the ``do_matmul`` task which has a constraint of one CPU and one GPU. This task
first transfers the necessary data to the GPU using Numba's ``cuda`` module,
then invokes the ``matmul`` function (that is decorated with
the Numba's ``@cuda.jit`). When the execution in the GPU of the
``matmul`` finishes, the result is transferred to the cpu with
the ``copy_to_host`` function and the task result is returned.


.. code-block:: python
    :name: numba_gpus
    :caption: Task using Numba and a GPU

    import math
    from numba import cuda, float64
    import numpy as np
    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on
    from pycompss.api.constraint import constraint

    TPB = 16

    @cuda.jit
    def matmul(A, B, C):
        """Perform square matrix multiplication of C = A * B
        """
        i, j = cuda.grid(2)
        if i < C.shape[0] and j < C.shape[1]:
            tmp = 0.
            for k in range(A.shape[1]):
                tmp += A[i, k] * B[k, j]
            C[i, j] = tmp

    @constraint(processors=[{'ProcessorType':'CPU', 'ComputingUnits':'1'},
                            {'ProcessorType':'GPU', 'ComputingUnits':'1'}])
    @task(returns=1)
    def do_matmul(a, b, c):
        gpu_a = cuda.to_device(a)
        gpu_b = cuda.to_device(b)
        gpu_c = cuda.to_device(c)

        threadsperblock = (TPB, TPB)
        blockspergrid_x = math.ceil(gpu_c.shape[0] / threadsperblock[0])
        blockspergrid_y = math.ceil(gpu_c.shape[1] / threadsperblock[1])
        blockspergrid = (blockspergrid_x, blockspergrid_y)

        matmul[blockspergrid, threadsperblock](gpu_a, gpu_b, gpu_c)
        c = gpu_c.copy_to_host()
        return c

    def main():
        a = np.random.uniform(1, 2, (4, 4))
        b = np.random.uniform(1, 2, (4, 4))
        c = np.zeros((4, 4))

        result = do_matmul(a, b, c)
        result = compss_wait_on(result)

        print("a: \n %s" % str(a))
        print("b: \n %s" % str(b))
        print("Result: \n %s" % str(result))

        print("Verification result: ")
        print(a @ b)


    if __name__=="__main__":
        main()


.. CAUTION::

    The function compiled with Numba for GPU can not be a task since the
    step to transfer the data to the GPU and backwards needs to be explicitly
    performed by the user.

    For this reason, the appropriate structure is composed by a task that
    has the necessary constraints, deals with the data movements and invokes
    the function compiled with Numba for GPU.

    The main application can then invoke the task.


.. IMPORTANT::

    In order to run with GPUs in local machine, you need to define the available
    GPUs in the ``project.xml`` file.

    As example, the following ``project.xml`` and ``resources.xml`` shall be
    used with the ``--project`` and ``--resources`` correspondingly:

    * :download:`project.xml <./01_Task_decorator/Resources/project.xml>`
    * :download:`resources.xml <./01_Task_decorator/Resources/resources.xml>`


More details about Numba and the specification of the signature, declaration
and flags can be found in the Numba's webpage
(http://numba.pydata.org/).
