Integration with Numba
----------------------

PyCOMPSs can also be used with Numba. Numba (http://numba.pydata.org/)
is an Open Source JIT compiler for Python which provides a set of
decorators and functionalities to translate Python functios to optimized
machine code.

Basic usage
~~~~~~~~~~~

PyCOMPSs’ tasks can be decorated with Numba’s
``@jit``/\ ``@njit`` decorator (with the appropiate
parameters) just below the @task decorator in order to apply
Numba to that task.

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
    True: Applies *jit* to the function.

- **Dictionary{k, v}**:
    Applies *jit* with the dictionary parameters to the function
    (allows to specify specific jit parameters (e.g.*nopython=True*)).

- **String**:
    - "jit": Applies *jit* to the function.
    - "njit": Applies *jit* with *nopython=True* to the function.
    - "generated_jit": Applies *generated_jit* to the function.
    - "vectorize": Applies *vectorize* to the function. Needs some extra flags in the *@task* decorator:

      - *numba_signature*: String with the *vectorize* signature.

    - "guvectorize": Applies *guvectorize* to the function. Needs some extra flags in the *@task* decorator:

      - *numba_signature*: String with the *guvectorize* signature.
      - *numba_declaration*: String with the *guvectorize* declaration.

    - "stencil": Applies *stencil* to the function.
    - "cfunc": Applies   *cfunc* to the function. Needs some extra flags in the *@task* decorator:

      - *numba_signature*: String with the *cfunc* signature.

Moreover, the *@task* decorator also allows to define specific
flags for the *jit*, *njit*, *generated_jit*, *vectorize*,
*guvectorize* and *cfunc* functionalities with the *numba_flags* hint.
This hint is used to declare a dictionary with the flags expected to use
with these numba functionalities. The default flag included by PyCOMPSs
is the *cache=True* in order to exploit the function caching of Numba
across tasks.

For example, to apply Numba *jit* to a task:

.. code-block:: python

    from pycompss.api.task import task

    @task(numba='jit')  # Aternatively: @task(numba=True)
    def jit_func(a, b):
         ...

And if the developer wants to use specific flags with *jit* (e.g.
*parallel=True*), the *numba_flags* must be defined with a dictionary where
the key is the numba flag name, and the value, the numba flag value to use):

.. code-block:: python

    from pycompss.api.task import task

    @task(numba='jit', numba_flags={'parallel':True})
    def jit_func(a, b):
         ...

Other Numba’s functionalities require the specification of the function
signature and declaration. In the next example a task that will use the
*vectorize* with three parameters and a specific flag to target the cpu
is shown:

.. code-block:: python

    from pycompss.api.task import task

    @task(returns=1,
          numba='vectorize',
          numba_signature=['float32(float32, float32, float32)'],
          numba_flags={'target':'cpu'})
    def vectorize_task(a, b, c):
        return a * b * c

Details about numba and the specification of the signature, declaration
and flags can be found in the Numba’s webpage
(http://numba.pydata.org/).
