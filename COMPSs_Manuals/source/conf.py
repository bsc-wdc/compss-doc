#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# COMPSs documentation build configuration file, created by
# sphinx-quickstart on Thu Oct  3 13:27:53 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.imgmath',
              'sphinx.ext.ifconfig',
              'sphinx.ext.imgconverter',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.mathjax',
              'sphinxcontrib.contentui',
              #'sphinx_simplepdf',  # Potential replacement for pdf generation
              'nbsphinx',
              #'myst_nb',  # Alternative to nbsphinx
              'sphinx_design',
              'sphinx_copybutton',
              'sphinxcontrib.rsvgconverter',
              'sphinxcontrib.youtube',
              'sphinx_tabs.tabs',
              'sphinx_toolbox.collapse',
              'sphinxcontrib.spelling']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'
#source_suffix = {'.rst': 'restructuredtext',
#                 '.ipynb': 'myst-nb',
#                 '.myst': 'myst-nb',
#}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'COMPSs'
copyright = 'Barcelona Supercomputing Center (BSC)'
author = 'Workflows and Distributed Computing Group (WDC)'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '3.3.3'
# The full version, including alpha/beta/rc tags.
release = '3.3.3'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default' # 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# True to prefix each section label with the name of the document it is in,
# followed by a colon.
autosectionlabel_prefix_document = True

# Specific configuration
numfig = True
numfig_secnum_depth = 0
numfig_format = {'figure':'Figure %s',
                 'table':'Table %s',
                 'code-block':'Code %s',
                 'section':'Section %s'}
html_permalinks = False  # Disabled permalinks
html_logo = './Logos/COMPSs_logo_small.png'
html_show_sourcelink = False
html_show_copyright = True
html_show_sphinx = True
html_favicon = './Logos/COMPSs_logo.ico'
nitpicky = True
latex_logo = './Logos/COMPSs_logo.png'

# Disable notebooks Building
nb_execution_mode = 'off'

nbsphinx_execute = 'never'
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]
# Do not allow building if execution is enabled and a notebook fails
nbsphinx_allow_errors = True
nbsphinx_requirejs_path = ''

# Disable tabs can be closed by selecting the open tab
sphinx_tabs_disable_tab_closing = True

# Spelling configuration
spelling_lang='en'
tokenizer_lang='en'
spelling_word_list_filename='spelling_wordlist.txt'
spelling_exclude_patterns=['ignored_*']
spelling_show_suggestions=True
spelling_suggestion_limit=0
spelling_show_whole_line=True
spelling_warning=True
spelling_verbose=True
spelling_ignore_pypi_package_names=True
spelling_ignore_wiki_words=True
spelling_ignore_acronyms=True
spelling_ignore_python_builtins=True
spelling_ignore_importable_modules=True
spelling_ignore_contributor_names=True
spelling_filters=[]


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme' # 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {'logo_only': True,
                      'navigation_depth': 8}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']

# html_context = {
#     'css_files': ['_static/_theme_overrides.css',  # override wide tables in RTD theme
#                  ],
# }

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'COMPSsdoc'

html_scaled_image_link = False


# -- Options for Youtube in latex output ------------------------------------------
youtube_cmd = r"\newcommand{\sphinxcontribyoutube}[3]{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}" + "\n"
latex_elements = {"preamble": youtube_cmd}


# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'pdflatex'
latex_additional_files = ['./_static/bsc_logo.jpg']
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',
    'releasename':" ",
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    # 'fncychap': '\\usepackage[Lenny]{fncychap}',
    'fncychap': '\\usepackage{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',

    'figure_align':'htbp',
    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
        %%%%%%%%%%%%%%%%%%%% PREAMBLE %%%%%%%%%%%%%%%%%%
        %%% Add number to subsubsection 2=subsection, 3=subsubsection
        %%% Below subsubsection is not good idea.
        \setcounter{secnumdepth}{3}

        %%% Table of content upto 2=subsection, 3=subsubsection
        \setcounter{tocdepth}{2}

        %%% Load packages
        \usepackage{amsmath,amsfonts,amssymb,amsthm}
        \usepackage{graphicx}
        % \usepackage[strings]{underscore}

        %%% Reduce spaces for Table of contents, figures and tables-
        %%% It is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
        \usepackage[notlot,nottoc,notlof]{}

        \usepackage{color}
        \usepackage{transparent}
        \usepackage{eso-pic}
        \usepackage{lipsum}

        %%% Link at the footnote to go to the place of footnote in the text
        \usepackage{footnotebackref}
        \makeatletter
        \LetLtxMacro{\BHFN@Old@footnotemark}{\@footnotemark}

        \renewcommand*{\@footnotemark}{%
            \refstepcounter{BackrefHyperFootnoteCounter}%
            \xdef\BackrefFootnoteTag{bhfn:\theBackrefHyperFootnoteCounter}%
            \label{\BackrefFootnoteTag}%
            \BHFN@Old@footnotemark
        }
        \makeatother

        %%% Spacing between line
        \usepackage{setspace}
        %%%% \onehalfspacing
        %%%% \doublespacing
        \singlespacing

        %%% Datetime
        \usepackage{datetime}
        \newdateformat{MonthYearFormat}{%
            \monthname[\THEMONTH], \THEYEAR}

        %% RO, LE will not work for 'oneside' layout.
        %% Change oneside to twoside in document class
        \usepackage{fancyhdr}
        \pagestyle{fancy}
        \fancyhf{}

        %%% Alternating Header for oneside
        \fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{ \small \nouppercase{\leftmark} }{}}
        \fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{}{ \small \nouppercase{\rightmark} }}

        %%% Alternating Header for two side
        %\fancyhead[RO]{\small \nouppercase{\rightmark}}
        %\fancyhead[LE]{\small \nouppercase{\leftmark}}

        %%% For oneside: change footer at right side. If you want to use Left and right then use same as header defined above.
        \fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{{\tiny BSC-WDC Group} }{\href{http://www.bsc.es}{\tiny BSC}}}

        %%% Alternating Footer for two side
        %\fancyfoot[RO, RE]{\scriptsize BSC-WDC Group (support-compss@bsc.es)}

        %%% page number
        \fancyfoot[CO, CE]{\thepage}

        \renewcommand{\headrulewidth}{0.5pt}
        \renewcommand{\footrulewidth}{0.5pt}

        \RequirePackage{tocbibind} %%% comment this to remove page number for following
        \addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
        \addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
        \addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
        % \addto\captionsenglish{\renewcommand{\chaptername}{Chapter}}

        %%% Reduce spacing for itemize
        \usepackage{enumitem}
        \setlist{nosep}

        %%% Quote Styles at the top of chapter
        \usepackage{epigraph}
        \setlength{\epigraphwidth}{0.8\columnwidth}
        \newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
        %%% Quote for all places except Chapter
        \newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}

        %%%%%%%%%%%%%%%%%% END PREAMBLE %%%%%%%%%%%%%%%%%
    ''',

    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering

            \vspace*{40mm} %%% * is used to give space from top
            %%% \textbf{\Huge {Title over the logo}}

            \vspace{0mm}
            \begin{figure}[!h]
             \centering
             \includegraphics[scale=0.4]{COMPSs_logo.png}
            \end{figure}

            \vspace{0mm}
            \Huge \textbf{{COMPSs Manual}}

            \Large Workflows and Distributed Computing Group
            \vspace{0mm}
            \begin{figure}[!h]
             \centering
             \includegraphics[scale=0.3]{bsc_logo.jpg}
            \end{figure}

            \vspace*{20mm}
            \large  Last updated : \MonthYearFormat\today

            %% \vfill adds at the bottom
            \vfill
            \normalsize \textit{Online version available at }{\href{https://compss-doc.readthedocs.io/en/latest/}{COMPSs - ReadTheDocs}}
        \end{titlepage}

        \clearpage
        \pagenumbering{roman}
        \tableofcontents
        \listoffigures
        \listoftables
        \clearpage
        \pagenumbering{arabic}

        ''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'sphinxsetup': \
        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        HeaderFamily=\\rmfamily\\bfseries, \
        InnerLinkColor={rgb}{0,0,1}, \
        OuterLinkColor={rgb}{0,0,1}',

        'tableofcontents':' ',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'COMPSs.tex', 'COMPSs Documentation',
    'Workflows and Distributed Computing Group (WDC)', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'compss', 'COMPSs Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'COMPSs', 'COMPSs Documentation',
     author, 'COMPSs', 'COMPSs Manuals.',
     'Programming Model'),
]
