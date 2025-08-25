Use of programming models inside tasks
**************************************

To improve COMPSs performance in some cases, C/C++ binding offers the
possibility to use programming models inside tasks. This feature allows
the user to exploit the potential parallelism in their application's
tasks.

OmpSs
=====

COMPSs C/C++ binding supports the use of the programming model OmpSs. To
use OmpSs inside COMPSs tasks we have to annotate the implemented tasks.
The implementation of tasks was described in section
[sec:functionsfile]. The following code shows a COMPSs C/C++ task
without the use of OmpSs.

.. code-block:: C

    void compss_task(int* a, int N) {
      int i;
      for (i = 0; i < N; ++i) {
      	a[i] = i;
      }
    }

This code will assign to every array element its position in it. A
possible use of OmpSs is the following.

.. code-block:: C

    void compss_task(int* a, int N) {
      int i;
      for (i = 0; i < N; ++i) {
       #pragma omp task
       {
        a[i] = i;
       }
      }
    }

This will result in the parallelization of the array initialization, of
course this can be applied to more complex implementations and the
directives offered by OmpSs are much more. You can find the
documentation and specification in https://pm.bsc.es/ompss.

There's also the possibility to use a newer version of the OmpSs
programming model which introduces significant improvements, OmpSs-2.
The changes at user level are minimal, the following image shows the
array initialization using OmpSs-2.

.. code-block:: C

    void compss_task(int* a, int N) {
        int i;

        for (i = 0; i < N; ++i) {
         #pragma oss task
         {
          a[i] = i;
         }
        }
    }

Documentation and specification of OmpSs-2 can be found in
https://pm.bsc.es/ompss-2.
