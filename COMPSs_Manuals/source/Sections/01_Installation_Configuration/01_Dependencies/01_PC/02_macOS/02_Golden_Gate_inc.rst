**macOS Golden Gate** dependencies installation commands:

Although many packages can be installed with Homebrew, some of them will have to be installed manually
from their source files. It is also important to mention that, some package names may be slightly different
in Homebrew, compared to Linux distributions, thus, some previous search for equivalences may be required.
Our tested installation sequence was as follows. Please install each package **INDIVIDUALLY**, since some can
have post-installation instructions that require adding environment variables to your shell profile.

.. code-block:: console

    brew install openjdk@21
    sudo ln -sfn /opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-21.jdk
    brew install graphviz
    brew install libxslt
    brew install xmlto
    brew install lynx
    brew install libtool
    brew install automake
    brew install coreutils
    brew install util-linux
    brew install boost
    brew install gradle
    echo 'export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"' >> ~/.bashrc
    export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
    echo 'export JAVA_HOME="/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home"' >> ~/.bashrc
    export JAVA_HOME="/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home"
    echo 'export GRADLE_HOME="/opt/homebrew/opt/gradle/libexec"' >> ~/.bashrc
    export GRADLE_HOME="/opt/homebrew/opt/gradle/libexec"
    echo 'export PATH="$GRADLE_HOME/bin:$PATH"' >> ~/.bashrc
    export PATH="$GRADLE_HOME/bin:$PATH"


The package ``xdg-utils`` has to be installed by hand (after installing ``libxslt``, ``xmlto`` and ``lynx``):

.. code-block:: console

    export XML_CATALOG_FILES="/opt/homebrew/etc/xml/catalog"
    git clone --branch v1.2.1 https://gitlab.freedesktop.org/xdg/xdg-utils.git
    cd xdg-utils
    ./configure --prefix=/usr/local
    make && make install


You can download the following script for your reference, but we **STRONGLY** recommend to run it command by
command, since every installation step with ``brew`` usually includes post-installation instructions.

.. literalinclude:: ./01_PC/02_macOS/02_Golden_Gate/COMPSs_deps_Golden_Gate_27_0.sh
    :language: bash

:download:`this example script <./01_PC/02_macOS/02_Golden_Gate/COMPSs_deps_Golden_Gate_27_0.sh>`

.. WARNING::

    Tracing is not yet available for macOS, therefore, its dependencies do not need
    to be installed.