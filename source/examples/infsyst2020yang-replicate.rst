.. _examples_infsyst2020yang-replicate:

"OrgMining 2.0": replicate the experiments
==========================================

This page presents the guide for replicating the major part of 
experiments in the paper [yang2020]_.

.. note::
   Before proceeding, make sure you have installed OrgMiner on your 
   machine. (:ref:`How to install? <install>`)

Download and extract the bundled zip from 
`HERE <https://github.com/roy-jingyang/infsyst-2020-Yang_OrgMining/archive/master.zip>`_,
**navigate to folder** ``experiment/``, in which you would find the 
following files:

.. code-block:: bash

    .
    ├── batch.py
    ├── configs
    │   ├── final
    │   │   ├── bpic17.graphml
    │   │   └── wabo.graphml
    │   └── complete
    │       ├── bpic17.graphml
    │       └── wabo.graphml
    ├── data
    │   ├── bpic17.xes
    │   └── wabo.xes
    ├── data.zip
    ├── execute.py
    └── trace_clustering_reports
        ├── bpic17.bosek14.tcreport
        └── wabo.bosek5.tcreport

These enables replicating the major part of the experiments in the 
paper (i.e., those reported in Sect. 6.3.1. "Global Conformance 
Analysis"). 

Compressed archive ``data.zip`` contains the 2 event logs used in the 
experiments. Folder ``configs`` contains the configuration files with 
respect to the 2 event logs. Folder ``trace_clustering_reports`` 
contains the trace clustering results generated from applying the 
Context Aware Trace Clustering technique [bose2009]_ ("Guide Tree Miner" 
in `ProM 6 <http://www.promtools.org/doku.php>`_) which are prepared for 
the experiments.

Please follow the steps below to conduct the experiments.

1. Prepare the experiment dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Decompress ``data.zip`` under the current folder, which should produce 
a folder ``data/`` with 2 event log files in IEEE XES format.

.. code-block:: bash

    data
    ├── bpic17.xes
    └── wabo.xes

Note that these log files have been preprocessed accordingly (see Sect. 
6.1 in the paper).

2. (Optional) Edit the experiment setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Navigate to folder ``configs/``, you will find 2 subfolders:

.. code-block:: bash

    configs/
    ├── final
    │   ├── bpic17.graphml
    │   └── wabo.graphml
    └── complete
        ├── bpic17.graphml
        └── wabo.graphml

From here we offer two options for those who wish to replicate the 
experiments:

* using the configuration files under folder ``final/``, which 
  correspond to the final results as reported in the paper. Settings 
  stored in these files were derived after we had finished all the 
  parameter searches and determine the values. For this option, please 
  proceed to :ref:`examples_infsyst2020yang-replicate_final`.
* using the configuration files under folder ``complete/``, which should 
  replicate the whole process. For this option, please proceed to
  :ref:`examples_infsyst2020yang-replicate_complete`.

For either of these options, you can choose to view and edit the 
configuration files with diagramming. 
To do so, we recommend using 
`Gephi <https://gephi.org/>`_ (other graph visualization software should 
suffice as long as it supports the 
`GraphML format <https://gephi.org/users/supported-graph-formats/graphml-format/>`_ 
used for recording the configuration):

1. Load a configuration file with extension ``.graphml`` using Gephi.
2. (Optional) Toggle on "Show Node Labels" (by clicking on the **T** 
   button on the bottom-left corner) for better visualization.
3. Edit the edge connections to determine which methods should be 
   combined for model discovery.
4. Switch to "Data Laboratory" tab for viewing and editing the parameter 
   settings for each of the methods.
5. Use "File->Export->Graph file" to save the new configuration file as 
   GraphML format.


.. _examples_infsyst2020yang-replicate_final:

3a. Reproduce the final results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_ 
(or the terminal for Unix-like systems), change to the current directory.

Type

``python batch.py ./configs/final/wabo.graphml [path_to_output_folder]``

with path to a folder holding the output files specified.

Change the file name of the input configuration to ``bpic17.graphml`` to 
run the experiments on another event log.

.. _examples_infsyst2020yang-replicate_complete:

3b. Run the complete experiments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
    Due to the parameter searching procedures when running the complete 
    experiments (as elaborated in Sect. 6.2 in the paper), long 
    computation time may be expected.

Open an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_ 
(or the terminal for Unix-like systems), change to the current directory.

Type

``python batch.py ./configs/complete/wabo.graphml [path_to_output_folder]``

with path to a folder holding the output files specified.

Change the file name of the input configuration to ``bpic17.graphml`` to 
run the experiments on another event log.

4. Check the experiment results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The experiments will be conducted automatically according to the 
configuration file provided. After completion, you may find two types of 
files under the specified output folder:

* ``*.om``, output organizational model, of which the file name shows 
  the corresponding methods used for discovering the model.
* ``.*_report.csv``, number of groups, fitness, precision values of the 
  corresponding model.

