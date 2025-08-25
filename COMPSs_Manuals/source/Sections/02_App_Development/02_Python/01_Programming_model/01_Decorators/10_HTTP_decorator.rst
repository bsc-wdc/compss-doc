@http
=====

The *@http* decorator can be used for the tasks to be executed on a remote
Web Service via HTTP requests. In order to create HTTP tasks, it is obligatory to
define HTTP resource(s) in ``resources`` and ``project`` files (see
:ref:`http_configuration`).
Following code snippet (:numref:`http_task_python_basic`) is a basic HTTP task
with all required parameters. At the time of execution, the runtime will search
for HTTP resource from resources file which allows execution of 'service_1' and
send a GET request to its 'Base URL'. Moreover, python parameters can be added to
the request query as shown in the example (between double curly brackets).

Definition
----------

.. code-block:: python
    :name: http_task_python_basic
    :caption: HTTP Task example.

    from pycompss.api.task import task
    from pycompss.api.http import http

    @http(service_name="service_1", request="GET",
          resource="get_length/{{message}}")
    @task(returns=int)
    def an_example(message):
        pass


For POST requests it is possible to  send a parameter as the request body by adding
it to the ``payload`` arg. In this case, payload type can also be
specified ('application/json' by default). If the parameter is a FILE type, then
the content of the file is read in the master and added to the request as request
body.


.. code-block:: python
    :name: http_task_python_post
    :caption: HTTP Task with POST request.

    from pycompss.api.task import task
    from pycompss.api.http import http

    @http(service_name="service_1", request="POST", resource="post_json/",
          payload="{{payload}}", payload_type="application/json")
    @task(returns=str)
    def post_with_param(payload):
        pass


For the cases where the response body is a JSON formatted string, PyCOMPSs' HTTP
decorator allows response string formatting by defining the return values within
the ``produces`` parameter. In the following example, the return value of the task
would be extracted from 'length' key of the JSON response string:


.. code-block:: python
    :name: http_task_python_produces
    :caption: HTTP Task with return value to be extracted from a JSON string.

    from pycompss.api.task import task
    from pycompss.api.http import http


    @http(service_name="service_1", request="GET",
          resource="produce_format/{{message}}",
          produces="{'length':'{{return_0}}'}")
    @task(returns=int)
    def an_example(message):
        pass

Note that if the task has multiple returns, 'return_0', 'return_1', return_2, etc.
all must be defined in the ``produces`` string.


It is also possible to take advantages of INOUT python dicts within HTTP tasks. In this case, ``updates`` string can be used to update the INOUT dict:

.. code-block:: python
    :name: http_task_python_updatesSections/08_PyCOMPSs_Notebooks/demos/Mandelbrot_numba.ipynb
    :caption: HTTP Task with return value to be extracted from a JSON string.

    @http(service_name="service_1", request="GET",
          resource="produce_format/test",
          produces="{'length':'{{return_0}}', 'child_json':{'depth_1':'one', 'message':'{{param}}'}}",
          updates='{{event}}.some_key = {{param}}')
    @task(event=INOUT)
    def http_updates(event):
        """
        """
        pass

In the example above, 'some_key' key of the INOUT dict param will be updated according to the response. Please note that the ``{{param}}`` is defined inside ``produces``. In other words,
parameters that are defined inside ``produces`` string can be used in ``updates`` to update INOUT dicts.


.. IMPORTANT::

    **Disclaimer:** Due to serialization limitations, with the current implementation, outputs of regular PyCOMPSs ``tasks`` cannot be passed as input parameters to ``http`` tasks.

    **Disclaimer:** COLLECTION_* and DICTIONARY_* type of parameters are not supported within HTTP tasks. However, Python lists and dictionary objects can be used.
