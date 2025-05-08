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

<p align="center"><b>
    <a href="https://compss-doc.readthedocs.io/en/stable/index.html">Website</a>
    <a href="https://github.com/bsc-wdc/compss-doc">Releases</a>
    <a href="https://bit.ly/bsc-wdc-community">Slack</a>
</b></p>

COMP Superscalar (COMPSs) is a programming model which aims to ease the
development of applications for distributed infrastructures, such as Clusters,
Grids and Clouds. COMP Superscalar also features a runtime system that exploits
the inherent parallelism of applications at execution time.

This repository contains the COMPSs documentation ready to be built into
html (with/for the readTheDocs format).


<!-- SECTIONS -->

<!-- BUILDING COMPSS -->
# Building COMPSs documentation

Follow the next steps to build COMPSs in your current machine.

**IMPORTANT:** **Steps 1 and 2 have to be done only ONCE** while the next
steps will have to be repeated in a loop for every documentation modification.

## 1. Dependencies

The dependencies **MUST** be installed before building, and it is only necessary once.

* System dependencies

  * For Ubuntu:
    ```
    sudo apt-get install python3 pandoc myspell-en
    python3 -m pip install virtualenv
    ```
  * For OpenSuse:

    ```
    sudo zypper install python3 pandoc myspell-en
    python3 -m pip install virtualenv
    ```

## 2. Clone the current repository

```
git clone https://gitlab.bsc.es/wdc/documents/documentation.git
```

## 3. Go to the documentation folder

```
cd documentation/COMPSs_documentation
```

## 4. Add/modify/remove documentation contents

### 4.1. Create a new branch

First, create a git branch with a name describing the work:
```
git checkout -b "BRANCH_NAME"
```

### 4.1. Update the sources

* Add new contents:
    1. Go to `source/Sections/` and locate the place where you want to add
    a new file.
    2. Add a new file with `.rst` extension.
    3. Populate the file with the new content.
    4. Add a reference to the new file in the section index.
* Modify existing documentation:
    1. Go to `source/Sections/` and locate the file that you want to modify.
    2. Edit the file.
* Remove contents:
    1. Go to `source/Sections/` and locate the file that you want to delete.
    2. Delete the file
    3. Remove the reference to the file on its section index.

### 4.2 Build the documentation

This step builds the documentation so that it can be checked locally.
Execute:
```
./build.sh
```

**IMPORTANT:** The building output remarks any issue with **RED** lines. Please, **MAKE SURE TO FIX ALL OF THEM BEFORE CONTINUING**.

And visualize the output:
```
firefox build/html/index.html
```

### 4.3 Commit the changes

Now add the changes, commit them, and push it to gitlab:
```
git add ./sources/path/to/modifications
git commit -m "Message describing the changes"
git push -u origin BRANCH_NAME
```

**IMPORTANT:** Go back to step 4.1 in order to do the next modification within
the same git branch. Each loop across these three steps is intended to contain
a specific action on the documentation.

### 4.4 Rebase the branch

Once all modifications have been committed, it is time to rebase the branch
to ensure that all changes do not have conflict when merging.
```
git pull --rebase origin master
```
If the rebase ends successfully, go to step 4.5.
Otherwise, if conflicts appear, please, fix them and iterate over:
```
git add ./path/to/modified/files
git rebase --continue
```

### 4.5 Merge the branch

1. Go to documentation's gitlab (<https://gitlab.bsc.es/wdc/documents/documentation>).
2. Create a new merge request for your branch.
3. Click on merge.

And the branch should be merged in or internal gitlab repository.

## 5. Publish the documentation

In order to make the modifications visible to the public, the next step
is to launch the `compss-doc-github-mirroring` job in Jenkins:

1. Go to Jenkins `compss-doc-github-mirroring` job:
<https://compss.bsc.es/jenkins/view/Mirrorings/job/compss-doc-github-mirroring/>
2. Click on `Build with Parameters` (left panel).
3. Click on `Ejecución`

This triggers the mirror of our internal gitlab reporitory (for the master)
branch into the public github repository.

ReadTheDocs is already configured to detect any modification in the github
repository, so it will update the documentation automatically. This process
usually takes from 2-5 minutes. You can check the progress going to ReadTheDocs
and login with the COMPSs user (user and pass available in the documentation
wiki) and look into `Compilations`.

## 6. Clean local files

Once the whole process is finished, you can clean all your local folder (removes the virtual environment, built documentation and temporary files):
```
./clean.sh
```

# Contact

:envelope: COMPSs Support <support-compss@bsc.es> :envelope:

Workflows and Distributed Computing Group (WDC)

Department of Computer Science (CS)

Barcelona Supercomputing Center (BSC)


<!-- LINKS -->
[1]: http://compss.bsc.es
