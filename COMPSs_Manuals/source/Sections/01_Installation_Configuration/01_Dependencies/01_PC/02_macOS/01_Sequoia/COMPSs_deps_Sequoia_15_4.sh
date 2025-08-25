brew install openjdk@11
sudo ln -sfn /opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-11.jdk
brew install graphviz
brew install libxslt
brew install xmlto
brew install libtool
brew install automake
brew install coreutils
brew install util-linux
brew install boost
brew install gradle
export JAVA_HOME=$(dirname $(readlink $(which javac)))/java_home
echo $JAVA_HOME >> ~/.bashrc
echo 'export GRADLE_HOME=/opt/gradle-8.7' >> ~/.bashrc
export GRADLE_HOME=/opt/gradle-8.7
echo 'export PATH=/opt/gradle-8.7/bin:$PATH' >> ~/.bashrc
export PATH=/opt/gradle-8.7/bin:$PATH
# The package ``xdg-utils`` has to be installed by hand (after installing ``libxslt`` and ``xmlto``)
export XML_CATALOG_FILES="/usr/local/etc/xml/catalog"
git clone https://gitlab.freedesktop.org/xdg/xdg-utils.git
cd xdg-utils
./configure --prefix=/usr/local
make ; make install