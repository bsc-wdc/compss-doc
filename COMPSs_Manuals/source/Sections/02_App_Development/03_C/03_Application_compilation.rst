Application Compilation
-----------------------

To compile user’s applications with the C/C++ binding two commands are
used: The "\ **compss_build_app**\ ’ command allows to compile
applications for a single architecture, and the
"**compss_build_app_multi_arch**" command for multiple
architectures. Both commands must be executed in the directory of the
main application code.

Single architecture
~~~~~~~~~~~~~~~~~~~

The user command "**compss_build_app**" compiles both master and
worker for a single architecture (e.g. x86-64, armhf, etc). Thus,
whether you want to run your application in Intel based machine or ARM
based machine, this command is the tool you need.

Therefore, let’s see two examples, first, the application is going to be
build for the native architecture, in our case *x86-64*, and then for a
target architecture, for instance *armhf*. Please note that to use cross
compilation features and multiple architecture builds, you need to do
the proper installation of COMPSs, find more information in the builders
README.

When the target is the native architecture, the command to execute is
very simple;

.. code-block:: console

    $~/matmul_objects> compss_build_app Matmul
    [ INFO ] Java libraries are searched in the directory: /usr/lib/jvm/java-1.8.0-openjdk-amd64//jre/lib/amd64/server
    [ INFO ] Boost libraries are searched in the directory: /usr/lib/

    ...

    [Info] The target host is: x86_64-linux-gnu

    Building application for master...
    g++ -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Block.cc Matrix.cc
    ar rvs libmaster.a Block.o Matrix.o
    ranlib libmaster.a

    Building application for workers...
    g++ -DCOMPSS_WORKER -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Block.cc -o Block.o
    g++ -DCOMPSS_WORKER -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Matrix.cc -o Matrix.o
    ar rvs libworker.a Block.o Matrix.o
    ranlib libworker.a

    ...

    Command successful.

In order to build an application for a different architecture e.g.
*armhf*, an environment must be provided, indicating the compiler used
to cross-compile, and also the location of some COMPSs dependencies such
as java or boost which must be compliant with the target architecture.
This environment is passed by flags and arguments;

.. code-block:: console

    $~/matmul_objects> compss_build_app --cross-compile --cross-compile-prefix=arm-linux-gnueabihf- --java_home=/usr/lib/jvm/java-1.8.0-openjdk-armhf Matmul
    [ INFO ] Java libraries are searched in the directory: /usr/lib/jvm/java-1.8.0-openjdk-armhf/jre/lib/arm/server
    [ INFO ] Boost libraries are searched in the directory: /usr/lib/
    [ INFO ] You enabled cross-compile and the prefix to be used is: arm-linux-gnueabihf-

    ...

    [ INFO ] The target host is: arm-linux-gnueabihf

    Building application for master...
    g++ -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Block.cc Matrix.cc
    ar rvs libmaster.a Block.o Matrix.o
    ranlib libmaster.a

    Building application for workers...
    g++ -DCOMPSS_WORKER -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Block.cc -o Block.o
    g++ -DCOMPSS_WORKER -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Matrix.cc -o Matrix.o
    ar rvs libworker.a Block.o Matrix.o
    ranlib libworker.a

    ...

    Command successful.

*[The previous outputs have been cut for simplicity]*

The **--cross-compile** flag is used to indicate the users desire to
cross-compile the application. It enables the use of
**--cross-compile-prefix** flag to define the prefix for the
cross-compiler. Setting $CROSS_COMPILE environment variable will also
work (in case you use the environment variable, the prefix passed by
arguments is overrided with the variable value). This prefix is added to
*$CC* and *$CXX* to be used by the user *Makefile* and lastly by the
*GNU toolchain* . Regarding java and boost, **--java_home** and
**--boostlib** flags are used respectively. In this case, users can
also use teh *$JAVA_HOME* and *$BOOST_LIB* variables to indicate the
java and boost for the target architecture. Note that these last
arguments are purely for linkage, where *$LD_LIBRARY_PATH* is used by
*Unix/Linux* systems to find libraries, so feel free to use it if you
want to avoid passing some environment arguments.

Multiple architectures
~~~~~~~~~~~~~~~~~~~~~~

The user command "**compss_build_app_multi_arch**" allows a to
compile an application for several architectures. Users are able to
compile both master and worker for one or more architectures.
Environments for the target architectures are defined in a file
specified by ***c*\ fg** flag. Imagine you wish to build your
application to run the master in your Intel-based machine and the worker
also in your native machine and in an ARM-based machine, without this
command you would have to execute several times the command for a single
architecture using its cross compile features. With the multiple
architecture command is done in the following way.

.. code-block:: console

    $~/matmul_objects> compss_build_app_multi_arch --master=x86_64-linux-gnu --worker=arm-linux-gnueabihf,x86_64-linux-gnu Matmul

    [ INFO ] Using default configuration file: /opt/COMPSs/Bindings/c/cfgs/compssrc.
    [ INFO ] Java libraries are searched in the directory: /usr/lib/jvm/java-1.8.0-openjdk-amd64/jre/lib/amd64/server
    [ INFO ] Boost libraries are searched in the directory: /usr/lib/

    ...

    Building application for master...
    g++ -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Block.cc Matrix.cc
    ar rvs libmaster.a Block.o Matrix.o
    ranlib libmaster.a

    Building application for workers...
    g++ -DCOMPSS_WORKER -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Block.cc -o Block.o
    g++ -DCOMPSS_WORKER -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Matrix.cc -o Matrix.o
    ar rvs libworker.a Block.o Matrix.o
    ranlib libworker.a

    ...

    Command successful. # The master for x86_64-linux-gnu compiled successfuly

    ...

    [ INFO ] Java libraries are searched in the directory: /usr/lib/jvm/java-1.8.0-openjdk-armhf/jre/lib/arm/server
    [ INFO ] Boost libraries are searched in the directory: /opt/install-arm/libboost

    ...

    Building application for master...
    arm-linux-gnueabihf-g++ -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Block.cc Matrix.cc
    ar rvs libmaster.a Block.o Matrix.o
    ranlib libmaster.a

    Building application for workers...
    arm-linux-gnueabihf-g++ -DCOMPSS_WORKER -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Block.cc -o Block.o
    arm-linux-gnueabihf-g++ -DCOMPSS_WORKER -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Matrix.cc -o Matrix.o
    ar rvs libworker.a Block.o Matrix.o
    ranlib libworker.a

    ...

    Command successful. # The worker for arm-linux-gnueabihf compiled successfuly

    ...

    [ INFO ] Java libraries are searched in the directory: /usr/lib/jvm/java-1.8.0-openjdk-amd64/jre/lib/amd64/server
    [ INFO ] Boost libraries are searched in the directory: /usr/lib/

    ...

    Building application for master...
    g++ -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Block.cc Matrix.cc
    ar rvs libmaster.a Block.o Matrix.o
    ranlib libmaster.a

    Building application for workers...
    g++ -DCOMPSS_WORKER -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Block.cc -o Block.o
    g++ -DCOMPSS_WORKER -g -O3 -I. -I/Bindings/c/share/c_build/worker/files/ -c Matrix.cc -o Matrix.o
    ar rvs libworker.a Block.o Matrix.o
    ranlib libworker.a

    ...

    Command successful. # The worker for x86_64-linux-gnu compiled successfuly

*[The previous output has been cut for simplicity]*

Building for single architectures would lead to a directory structure
quite different than the one obtained using the script for multiple
architectures. In the single architecture case, only one master and one
worker directories are expected. In the multiple architectures case, one
master and one worker is expected per architecture.

.. code-block:: text

    .
    |-- arm-linux-gnueabihf
    |   `-- worker
    |       `-- gsbuild
    |           `-- autom4te.cache
    |-- src
    |-- x86_64-linux-gnu
    |   |-- master
    |   |   `-- gsbuild
    |   |       `-- autom4te.cache
    |   `-- worker
    |       `-- gsbuild
    |           `-- autom4te.cache
    `-- xml

    (Note than only directories are shown).

Using OmpSs
~~~~~~~~~~~

As described in section [sec:ompss] applications can use OmpSs and
OmpSs-2 programming models. The compilation process differs a little bit
compared with a normal COMPSs C/C++ application. Applications using
OmpSs must be compiled using the ``--ompss`` option in the
compss_build_app command.

.. code-block:: console

    $~/matmul_objects> compss_build_app --ompss Matmul

Executing the previous command will start the compilation of the
application. Sometimes due to configuration issues OmpSs can not be
found, the option ``--with_ompss=/path/to/ompss`` specifies the OmpSs
path that the user wants to use in the compilation.

Applications using OmpSs-2 are similarly compiled. The options to
compile with OmpSs-2 are ``--ompss-2`` and ``--with_ompss-2=/path/to/ompss-2``

.. code-block:: console

    $~/matmul_objects> compss_build_app --with_ompss-2=/home/mdomingu/ompss-2 --ompss-2 Matmul

Remember that additional source files can be used in COMPSs C/C++
applications, if the user expects OmpSs or OmpSs-2 to be used in those
files she, must be sure that the files are properly compiled with OmpSs
or OmpSs-2.
