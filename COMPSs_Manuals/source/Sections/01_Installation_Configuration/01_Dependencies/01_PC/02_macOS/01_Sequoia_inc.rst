**macOS Sequoia** dependencies installation commands:

Although many packages can be installed with Homebrew, some of them will have to be installed manually
from their source files. It is also important to mention that, some package names may be slightly different
in Homebrew, compared to Linux distributions, thus, some previous search for equivalences may be required.
Our tested installation sequence was as follows. Please install each package **INDIVIDUALLY**, since some can
have post-installation instructions that require adding environment variables to your shell profile.

.. code-block:: console

    $ brew install openjdk@11
    $ sudo ln -sfn /opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-11.jdk
    $ brew install graphviz
    $ brew install libxslt
    $ brew install xmlto
    $ brew install libtool
    $ brew install automake
    $ brew install coreutils
    $ brew install util-linux
    $ brew install boost
    $ brew install gradle
    $ export JAVA_HOME=$(dirname $(readlink $(which javac)))/java_home
    $ echo $JAVA_HOME >> ~/.bashrc
    $ echo 'export GRADLE_HOME=/opt/gradle-8.7' >> ~/.bashrc
    $ export GRADLE_HOME=/opt/gradle-8.7
    $ echo 'export PATH=/opt/gradle-8.7/bin:$PATH' >> ~/.bashrc
    $ export PATH=/opt/gradle-8.7/bin:$PATH


The package ``xdg-utils`` has to be installed by hand (after installing ``libxslt`` and ``xmlto``):

.. code-block:: console

    $ export XML_CATALOG_FILES="/usr/local/etc/xml/catalog"
    $ git clone https://gitlab.freedesktop.org/xdg/xdg-utils.git
    $ cd xdg-utils
    $ ./configure --prefix=/usr/local
    $ make ; make install

.. literalinclude:: ./01_PC/02_macOS/01_Sequoia/COMPSs_deps_Sequoia_15_4.sh
    :language: bash

:download:`this example script <./01_PC/02_macOS/01_Sequoia/COMPSs_deps_Sequoia_15_4.sh>`

.. WARNING::

    Tracing is not yet available for macOS, therefore, its dependencies do not need
    to be installed.