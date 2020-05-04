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
```
* Sphinx
```
pip3 install sphinx --user
# or
sudo pip3 install sphinx
```
* python3-Sphinx-latex
```
sudo zypper install python3-Sphinx-latex
```
* rst2pdf
```
pip3 install rst2pdf --user
# or
sudo pip3 install rst2pdf
```
* sphinxcontrib-svg2pdfconverter
```
pip3 install sphinxcontrib-svg2pdfconverter --user
# or
sudo pip3 install sphinxcontrib-svg2pdfconverter
```
* rsvg-view (rsvg-convert neede by sphinxcontrib-svg2pdfconverter)
```
sudo zypper install rsvg-view
```
* sphinxcontrib-bibtex
```
pip3 install sphinxcontrib-bibtex --user
# or
sudo pip3 install sphinxcontrib-bibtex
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
