.. _install:

*******
Install
*******

Prerequisites
=============
OrgMiner is built using Python, hence it is a prerequisite to have 
Python installed on your machine. 
We recommend using `Anaconda Python <https://docs.anaconda.com/anaconda/>`_, 
a distribution of Python featured with data science packages and 
enhanced support of package manager which will make life easier in 
resolving software dependencies. 

You may want to install only the minimal core of Anaconda Python: 
`Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_, as it 
will suffice the prerequisites.

Install OrgMiner
================
OrgMiner can be installed by directly using the Anaconda Python package
manager.

For Unix-like systems (Linux, MacOS), open the terminal; for Windows, 
open an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_.
Enter the following command

``conda install -c roy-jingyang orgminer``

should be able to install OrgMiner along with all necessary dependencies.

Optional Packages
=================
Some optional packages are needed for some main programs built upon 
OrgMiner, for example `Arya <https://github.com/roy-jingyang/OrgMiner-Arya>`_, 
a simple client-server application that provides an interactive way for 
organizational model discovery and visualization:

* Flask, a lightweight WSGI web application framework. 
* Graphviz, an open source graph visualization software.
* pygraphviz, a Python interface to Graphviz.

Use the following command to append these optional packages for OrgMiner:

``conda install -c roy-jingyang orgminer[arya]``

