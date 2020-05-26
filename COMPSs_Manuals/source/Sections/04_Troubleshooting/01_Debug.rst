How to debug
============

When the application does not behave as expected the first thing users
must do is to run it in **debug** mode executing the ``runcompss``
command withthe ``-d`` flag to enable the debug log level.

In this case the application execution will produce the following files:

-  ``runtime.log``

-  ``resources.log``

-  ``jobs`` folder

First, users should check the last lines of the runtime.log. If the
file-transfers or the tasks are failing an error message will appear in
this file. If the file-transfers are successfully and the jobs are
submitted, users should check the ``jobs`` folder and look at the error
messages produced inside each job. Users should notice that if there are
*RESUBMITTED* files something inside the job is failing.
