.. _install:

************
Installation
************

.. _install_prerequisites:

Install Prerequisites
=====================

Python
------
*OrdinoR* requires Python_ 3.7+. We recommend using Python 3.7 or 3.8.

PM4Py
-----
PM4Py_ is an open-source process mining platform written in Python. To
install PM4PY, please visit `PM4Py Installation`_.

..
  `Anaconda Python <https://docs.anaconda.com/anaconda/>`_ is a
  distribution of Python featured with data science packages and 
  enhanced support of package manager.
  
  You may wish to install the "mini" version of Anaconda Python,
  `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_, which 
  will suffice the prerequisites just as the 
  `complete installation <https://docs.anaconda.com/anaconda/install/>`_.

..
  Sidenote
  --------
  We are working on making the installation process easier, but still some 
  of the software dependencies need to be resolved manually. To do so, for 
  Unix-like systems (Linux, MacOS), open the terminal; for Windows, open 
  an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_.
  
  Enter the following commands, and confirm yes if prompted by conda.
  
  ``conda install --channel alubbock --channel conda-forge graphviz pygraphviz=1.5``
  
  (credits to `Alex Lubbock <https://anaconda.org/alubbock>`_ for 
  providing the conda recipe for resolving the dependencies on Windows)
  

.. _install_core:

Install OrdinoR
===============
*OrdinoR* is hosted on the Python Package Index `PyPI
<https://pypi.org/>`_, so you can use the following command to install
the core package.

``pip install ordinor``

.. _Python: https://www.python.org/
.. _PM4Py: https://pm4py.fit.fraunhofer.de/
.. _PM4Py Installation: https://pm4py.fit.fraunhofer.de/install
