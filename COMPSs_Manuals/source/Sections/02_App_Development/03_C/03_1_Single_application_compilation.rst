
The user command "**compss_build_app**" compiles both master and
worker for a single architecture (e.g. x86-64, armhf, etc). Thus,
whether you want to run your application in Intel based machine or ARM
based machine, this command is the tool you need.

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
