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
# The package ``xdg-utils`` has to be installed by hand (after installing ``libxslt``, ``xmlto`` and ``lynx``)
export XML_CATALOG_FILES="/opt/homebrew/etc/xml/catalog"
git clone --branch v1.2.1 https://gitlab.freedesktop.org/xdg/xdg-utils.git
cd xdg-utils
./configure --prefix=/usr/local
make && make install