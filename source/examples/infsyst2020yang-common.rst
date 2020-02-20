.. _examples_infsyst2020yang-common:

"OrgMining 2.0": organizational model mining framework
======================================================

This page presents the usage of several example programs used for the 
discovery and conformance checking of organizational models, along with 
the guide for replicating the major part of experiments in the paper 
[yang2020]_.

Source code of the these programs can be found in a 
`GitHub repository <https://github.com/roy-jingyang/infsyst-2020-Yang_OrgMining>`_.

.. note::
   Before proceeding, make sure you have installed OrgMiner on your 
   machine. (:ref:`How to install? <install>`)

How to Use
----------

Download and extract the bundled zip from 
`HERE <https://github.com/roy-jingyang/infsyst-2020-Yang_OrgMining/archive/master.zip>`_,
in which you would find the following files:

.. code-block:: bash

    .
    ├── experiment
    │   ├── batch.py
    │   ├── configs
    │   │   ├── bpic17.graphml
    │   │   └── wabo.graphml
    │   ├── execute.py
    │   └── trace_clustering_results
    │       ├── bpic17.bosek14.tcreport
    │       └── wabo.bosek5.tcreport
    ├── LICENSE
    ├── main
    │   ├── om_discover.py
    │   ├── om_evaluate.py
    │   └── om_toy_test.py
    ├── README.md
    └── tools
        ├── analyze_log.py
        ├── annotate_by_split_logs.py
        ├── om_grouping_stats.py
        └── om_search_k.py

The ``experiment/`` folder contains the necessary files for replicating 
the major part of the experiments. See :ref:`examples_infsyst2020yang-common_replicate` 
for more information.

The ``main/`` folder contains the main programs interacted via Command-Line 
Interface, and ``tools/`` contains some utility programs. See below for 
the usage of all these programs, respectively.

Discover an organizational model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_ 
(or the terminal for Unix-like systems), change to the ``main/`` 
directory (or move the main program to whichever folder you like as 
workspace), and run the program with the following command:

``python main.py [path_to_input_log_file] [path_to_output_model_file]``

by specifying paths to the input and output accordingly.

Log files of `IEEE XES <https://xes-standard.org/>`_ format are 
supported as input.

Output organizational models are stored in formatted texts, as shown 
below.

.. code-block:: bash


Check the conformance of an organizational model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test the "toy" model
^^^^^^^^^^^^^^^^^^^^


.. _examples_infsyst2020yang-common_replicate:

Replicate the experiments
-------------------------


