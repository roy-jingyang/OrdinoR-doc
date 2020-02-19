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

You may want to install only the mini version of Anaconda Python,
`Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_, which 
will suffice the prerequisites just as the 
`complete installation <https://docs.anaconda.com/anaconda/install/>`_.

Software Dependencies
---------------------
We are working on making the installation process easier, but still some 
of the software dependencies need to be resolved. To do so, for 
Unix-like systems (Linux, MacOS), open the terminal; for Windows, open 
an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_.
Enter the following command

``conda install --channel conda-forge igraph graphviz``

and confirm yes when prompted by conda.

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
following packages:

* Flask, a lightweight WSGI web application framework. 
* pygraphviz, a Python interface to Graphviz.

To resolve the depedencies for Arya, use the following command to append 
these optional packages:

``pip install orgminer[arya]``

