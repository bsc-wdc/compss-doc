python3 -m pip install --upgrade "sphinx==4.0.3" \
                       "sphinx-rtd-theme>=0.5.0rc1" \
                       myst-parser \
                       sphinxcontrib-contentui \
                       sphinx-copybutton \
                       sphinxcontrib-spelling \
                       nbsphinx \
                       sphinxcontrib.yt \
                       sphinxcontrib-svg2pdfconverter \
                       sphinx-panels \
                       git+https://github.com/executablebooks/sphinx-tabs \
                       git+https://github.com/sphinx-toolbox/sphinx-toolbox@master \
                       ipywidgets \
		       nbconvert \
		       --no-deps

echo "---- NOTE ----"
echo "Install pandoc, imagemagick, librsvg2-bin with your package manager"
echo "--------------"
