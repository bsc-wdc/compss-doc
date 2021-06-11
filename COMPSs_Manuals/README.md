<!-- LOGOS AND HEADER -->
<h1 align="center">
  <br>
  <a href="https://www.bsc.es/">
    <img src="source/Logos/bsc_280.png" alt="Barcelona Supercomputing Center" height="60px">
  </a>
  <a href="https://www.bsc.es/research-and-development/software-and-apps/software-list/comp-superscalar/">
    <img src="source/Logos/logo_compss.png" alt="COMP Superscalar" height="60px">
  </a>
  <br>
  <br>
  COMPSs Documentation
  <br>
</h1>

<h3 align="center">Component Superscalar framework and programming model for HPC.</h3>
<p align="center">
  <a href='http://bscgrid05.bsc.es/jenkins/job/COMPSs_Framework-Docker_testing'>
    <img src='http://bscgrid05.bsc.es/jenkins/job/COMPSs_Framework-Docker_testing/badge/icon'
         alt="Build Status">
  </a>
</p>

<p align="center"><b>
    <a href="https://www.bsc.es/research-and-development/software-and-apps/software-list/comp-superscalar/">Website</a>
    <a href="https://github.com/bsc-wdc/compss/releasess">Releases</a>
    <a href="https://bit.ly/bsc-wdc-community">Slack</a>
</b></p>

COMP Superscalar (COMPSs) is a programming model which aims to ease the development
of applications for distributed infrastructures, such as Clusters, Grids and Clouds.
COMP Superscalar also features a runtime system that exploits the inherent parallelism
of applications at execution time.

This repository contains the COMPSs documentation ready to be built into
pdf and html (with the readTheDocs format).


<!-- SECTIONS -->

<!-- BUILDING COMPSS -->
# Building COMPSs documentation

Follow the next steps to build COMPSs in your current machine.

## 1. Dependencies

* python3

```
sudo zypper install python3
# or
sudo apt-get install python3
```


Some OS do not include pip3 (e.g. Ubuntu, which provides just pip).
To make sure that you are using the Python 3 pip, create an alias:

```
alias pip3=`python3 -m pip`
```

* Python 3 dependencies
```
pip3 install sphinx --user
pip3 install sphinxcontrib.contentui --user
pip3 install six --upgrade
pip3 install nbsphinx --user
pip3 install sphinx-copybutton --user
pip3 install sphinxcontrib-svg2pdfconverter --user
pip3 install rst2pdf --user
pip3 install sphinxcontrib-bibtex --user
pip3 install pandoc --user
pip3 install ipywidgets --user
pip3 install sphinx-rtd-theme==0.5.0.rc1
pip3 install prompt-toolkit --user
pip3 install ipython --user
pip3 install sphinxcontrib.yt --user
```

* System dependencies

  * For Ubuntu:

  ```
  sudo apt-get install pandoc
  sudo apt-get install librsvg2-bin
  ```
  * For OpenSuse:

    ```
    sudo zypper install pandoc
    sudo zypper install python3-Sphinx-latex
    sudo zypper install rsvg-view
    ```

* Latex packages:

  * For Ubuntu:

  ````
  sudo apt install texlive-latex-extra
  sudo apt-get install -y latexmk
  ````
  *For OpenSuse:

    ```
    sudo zypper install texlive-footnotebackref texlive-datetime texlive-epigraph texlive-eso-pic texlive-lipsum texlive-footnotebackref texlive-setspace texlive-amsmath texlive-amsfonts texlive-amstex texlive-lipsum texlive-fancyhdr texlive-anyfontsize
    ```


## 2. Build COMPSs documentation

**Note**: Remember to install the dependencies before trying to build COMPSs
 from sources.

```
./build.sh
```

## 3. Building Issues

* Java lexer not found.

```
# Solution:
pip3 install prompt-toolkit --upgrade
pip3 install ipython --upgrade
# Check that the language is supported with:
pygmentize -L lexers
```

<!-- CONTACT -->
# Contact

:envelope: COMPSs Support <support-compss@bsc.es> :envelope:

Workflows and Distributed Computing Group (WDC)

Department of Computer Science (CS)

Barcelona Supercomputing Center (BSC)


<!-- LINKS -->
[1]: http://compss.bsc.es
