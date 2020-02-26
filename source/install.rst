.. _install:

************
Installation
************

Prerequisites
=============

Python
------
OrgMiner is built using Python, hence it is a prerequisite to have 
Python installed on your machine. 
We recommend using `Anaconda Python <https://docs.anaconda.com/anaconda/>`_, 
a distribution of Python featured with data science packages and 
enhanced support of package manager which will make life easier in 
resolving software dependencies. 

You may want to install only the "mini" version of Anaconda Python,
`Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_, which 
will suffice the prerequisites just as the 
`complete installation <https://docs.anaconda.com/anaconda/install/>`_.

Python 3 is expected to be used for OrgMiner. We have tested on 
Anaconda with Python version 3.6.x and 3.7.x.

Software Dependencies
---------------------
We are working on making the installation process easier, but still some 
of the software dependencies need to be resolved manually. To do so, for 
Unix-like systems (Linux, MacOS), open the terminal; for Windows, open 
an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_.

Enter the following commands, and confirm yes if prompted by conda.

``conda install --channel alubbock --channel conda-forge graphviz pygraphviz=1.5``

(credits to `Alex Lubbock <https://anaconda.org/alubbock>`_ for 
providing the conda recipe for resolving the dependencies on Windows)

Install OrgMiner
================
For Unix-like systems (Linux, MacOS), open the terminal; for Windows, 
open an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_.
Enter the following command

``pip install orgminer``

which should be able to install OrgMiner along with all remaining 
mandatory dependencies resolved.

.. _install_optional:

Optional Packages
=================
Some extra packages are needed for some main programs built upon 
OrgMiner.

For example, `Arya <https://github.com/roy-jingyang/OrgMiner-Arya>`_, 
a simple client-server application that provides an interactive way for 
organizational model discovery and visualization, relies on the 
following package(s):

* Flask, a lightweight WSGI web application framework. 

To resolve the depedencies for Arya, use the following command to append 
these optional package(s):

``pip install orgminer[arya]``

