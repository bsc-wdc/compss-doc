Known Limitations
=================

The current COMPSs version () has the following limitations:

-  **Exceptions:** The current COMPSs version is not able to propagate
   exceptions raised from a task to the master. However, the runtime
   catches any exception and sets the task as failed.

-  **Java tasks:** Java tasks **must** be declared as **public**.
   Despite the fact that tasks can be defined in the main class or in
   other ones, we recommend to define the tasks in a separated class
   from the main method to force its public declaration.

-  **Java objects:** Objects used by tasks must follow the *java beans*
   model (implementing an empty constructor and getters and setters for
   each attribute) or implement the *serializable* interface. This is
   due to the fact that objects will be transferred to remote machines
   to execute the tasks.

-  **Java object aliasing:** If a task has an object parameter and
   returns an object, the returned value must be a new object (or a
   cloned one) to prevent any aliasing with the task parameters.

   .. code-block:: java

       // @Method(declaringClass = "...")
       // DummyObject incorrectTask (
       //    @Parameter(type = Type.OBJECT, direction = Direction.IN) DummyObject a,
       //    @Parameter(type = Type.OBJECT, direction = Direction.IN) DummyObject b
       // );
       public DummyObject incorrectTask (DummyObject a, DummyObject b) {
           if (a.getValue() > b.getValue()) {
               return a;
           }
           return b;
       }

       // @Method(declaringClass = "...")
       // DummyObject correctTask (
       //    @Parameter(type = Type.OBJECT, direction = Direction.IN) DummyObject a,
       //    @Parameter(type = Type.OBJECT, direction = Direction.IN) DummyObject b
       // );
       public DummyObject correctTask (DummyObject a, DummyObject b) {
           if (a.getValue() > b.getValue()) {
               return a.clone();
           }
           return b.clone();
       }

       public static void main() {
           DummyObject a1 = new DummyObject();
           DummyObject b1 = new DummyObject();
           DummyObject c1 = new DummyObject();
           c1 = incorrectTask(a1, b1);
           System.out.println("Initial value: " + c1.getValue());
           a1.modify();
           b1.modify();
           System.out.println("Aliased value: " + c1.getValue());


           DummyObject a2 = new DummyObject();
           DummyObject b2 = new DummyObject();
           DummyObject c2 = new DummyObject();
           c2 = incorrectTask(a2, b2);
           System.out.println("Initial value: " + c2.getValue());
           a2.modify();
           b2.modify();
           System.out.println("Non-aliased value: " + c2.getValue());
       }

-  **Services types:** The current COMPSs version only supports SOAP
   based services that implement the WS interoperability standard. REST
   services are not supported.

-  **Use of file paths:** The persistent workers implementation has a
   unique *Working Directory* per worker. That means that tasks should
   not use hardcoded file names to avoid file collisions and tasks
   misbehaviours. We recommend to use files declared as task parameters,
   or to manually create a sandbox inside each task execution and/or to
   generate temporary random file names.

-  **Python constraints in the cloud:** When using python applications
   with constraints in the cloud the minimum number of VMs must be set
   to 0 because the initial VM creation doesn’t respect the tasks
   contraints. Notice that if no contraints are defined the initial VMs
   are still usable.

-  **Intermediate files**: Some applications may generate intermediate
   files that are only used among tasks and are never needed inside the
   master’s code. However, COMPSs will transfer back these files to the
   master node at the end of the execution. Currently, the only way to
   avoid transferring these intermediate files is to manually erase them
   at the end of the master’s code. Users must take into account that
   this only applies for files declared as task parameters and **not**
   for files created and/or erased inside a task.

-  **User defined classes in Python:** User defined classes in Python
   **must not be** declared **in the same file that contains the main
   method** (*if __name__==__main__'*) to avoid serialization
   problems of the objects.

-  **Python object hierarchy dependency detection**: Dependencies are
   detected only on the objects that are task parameters or outputs.
   Consider the following code:

   .. code-block:: python

       # a.py
       class A:
         def __init__(self, b):
           self.b  = b

       # main.py
       from a import A
       from pycompss.api.task import task
       from pycompss.api.parameter import *

       @task(obj = IN, returns = int)
       def get_b(obj):
         return obj.b

       @task(obj = INOUT)
       def inc(obj):
         obj += [1]

       def main():
         from pycompss.api.api import compss_wait_on
         my_a = A([5])
         inc(my_a.b)
         obj = get_b(my_a)
         obj = compss_wait_on(obj)
         print obj

       if __name__ == '__main__':
         main()

   Note that there should exist a dependency between ``A`` and ``A.b``.
   However, PyCOMPSs is not capable to detect dependencies of that kind.
   These dependencies must be handled (and avoided) manually.

-  **Python modules with global states**:Some modules (for example
   ``logging``) have internal variables apart from functions. These
   modules are not guaranteed to work in PyCOMPSs due to the fact that
   master and worker code are executed in different interpreters. For
   instance, if a ``logging`` configuration is set on some worker, it
   will not be visible from the master interpreter instance.

-  **Python global variables**:This issue is very similar to the
   previous one. PyCOMPSs does not guarantee that applications that
   create or modify global variables while worker code is executed will
   work. In particular, this issue (and the previous one) is due to
   Python’s Global Interpreter Lock (GIL).

-  **Python application directory as a module**: If the Python
   application root folder is a python module (i.e: it contains an
   ``__init__.py`` file) then ``runcompss`` must be called from the
   parent folder. For example, if the Python application is in a folder
   with an ``__init__.py`` file named ``my_folder`` then PyCOMPSs will
   resolve all functions, classes and variables as
   ``my_folder.object_name`` instead of ``object_name``. For example,
   consider the following file tree:

   .. code-block:: text

       my_apps/
       |- kmeans/
           |- __init__.py
           |- kmeans.py

   Then the correct command to call this app is
   ``runcompss kmeans/kmeans.py`` from the ``my_apps`` directory.

-  **Python early program exit**: All intentional, premature exit
   operations must be done with ``sys.exit``. PyCOMPSs needs to perform
   some cleanup tasks before exiting and, if an early exit is performed
   with ``sys.exit``, the event will be captured, allowing PyCOMPSs to
   perform these tasks. If the exit operation is done in a different way
   then there is no guarantee that the application will end properly.

-  **Python with numpy and MKL**: Tasks that invoke numpy and MKL may
   experience issues if tasks use a different number of MKL threads.
   This is due to the fact that MKL reuses threads along different calls
   and it does not change the number of threads from one call to
   another.
