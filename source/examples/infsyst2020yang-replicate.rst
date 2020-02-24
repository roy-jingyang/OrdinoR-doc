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
    │   ├── bpic17.graphml
    │   └── wabo.graphml
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

    data/
    ├── bpic17.xes
    └── wabo.xes

Note that these log files have been preprocessed accordingly (see Sect. 
6.1 in the paper).

2. (Optional) Edit the experiment setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Navigate to folder ``configs/``, you will find 2 configuration files:

.. code-block:: bash

    configs/
    ├── bpic17.graphml
    └── wabo.graphml

You can choose to view and edit the configuration files with 
diagramming. To do so, we recommend using 
`Gephi <https://gephi.org/>`_ (other graph visualization software should 
suffice as long as it supports the 
`GraphML format <https://gephi.org/users/supported-graph-formats/graphml-format/>`_ 
used for recording the configuration):

1. Load a configuration file with extension ``.graphml`` using Gephi.
2. (Optional) Toggle on "Show Node Labels" (by clicking on the **T** 
   button on the bottom-left corner) for better visualization.
   |fig:overview|
3. Edit the edge connections to determine which methods should be 
   combined for model discovery.
4. View and edit the parameter settings for each of the methods as node 
   attributes. For a brief instruction on how to alter the parameter 
   values, refer to :ref:`examples_infsyst2020yang-replicate_parameters`.
   |fig:edit|
5. Use "File->Export->Graph file" to save the new configuration file as 
   GraphML format. 
   |fig:export|

.. |fig:overview| image:: infsyst2020yang-replicate_gephi_overview.png
   :align: middle

.. |fig:edit| image:: infsyst2020yang-replicate_gephi_overview-edit.png
   :align: middle

.. |fig:export| image:: infsyst2020yang-replicate_gephi_overview-export.png
   :align: middle


3. Run the complete experiments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
    Due to the parameter searching procedures when running the complete 
    experiments (as elaborated in Sect. 6.2 in the paper), a long 
    computation time may be expected, especially for log "BPIC17" in the 
    dataset with 475306 events.

Open an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_ 
(or the terminal for Unix-like systems), change to the current directory.

Type

``python batch.py ./configs/wabo.graphml [path_to_output_folder]``

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


.. _examples_infsyst2020yang-replicate_parameters:

Appendix: Alter the parameter settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For **event log input**, the following parameter can be configured:

* ``filepath``: a string specifying the path to the input event log file 
  in IEEE XES format.

For **Execution Mode Learning** methods,

* ATonly: no configurable parameter.
* CT+AT+TT (case attribute):

    * ``case_attr_name``, a string specifying a case-level attribute in 
      the log used for deriving case types.
    * ``resolution``, a value of {``'hour'``, ``'day'``, ``'weekday'``}
      specifying a time unit used for deriving time types.

* CT+AT+TT (trace clustering):
    
    * ``fn_partition``, a string specifying the path to a file 
      containing the trace clustering results on the input log.
    * ``resolution``, a value of {``'hour'``, ``'day'``, ``'weekday'``}
      specifying a time unit used for deriving time types.

For **Resource Grouping discovery** methods,

* AHC:

    * ``n_groups``: a string in the format ``list(range(x, y))`` 
      specifying the range of possible number of resource groups to be 
      searched. Substitute ``x`` and ``y`` with actual integers desired. 
      Note that the range is defined as ``[x, y)``, i.e., non-inclusive on 
      the right side.
    * ``method``, a value of {``'ward'``, ``'complete'``, ``'average'``, 
      ``'single'``} specifying the linkage criterion. See 
      `Scikit-learn AHC method <https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering>`_ 
      for a reference.
    * ``metric``, a value of {``'euclidean'``, ``'cosine'``, 
      ``'correlation'``} specifying the distance metric.

* MOC:

    * ``n_groups``: a string in the format ``list(range(x, y))`` 
      specifying the range of possible number of resource groups to be 
      searched. Substitute ``x`` and ``y`` with actual integers desired. 
      Note that the range is defined as ``[x, y)``, i.e., non-inclusive on 
      the right side.

    * ``init``: a value of {``'random'``, ``'kmeans'``} specifying the 
      strategy used for initializing the parameters of MOC. With 
      ``'random'``, a random initialization with 100 runs is used; with 
      ``'kmeans'``, the seed is derived from first applying the kMeans 
      algorithm.


For **Execution Mode Assignment** methods,

* FullRecall: no configurable parameter.
* OverallScore:

    * ``w1``: a float number in range (0, 1) specifying the weighting 
      assigned to Group Relative Stake. When given, the weighting value 
      assigned to Group Coverage will be determined consequently as they 
      sum up to 1.0.

    * ``p``: a float number in range (0, 1) specifying the threshold 
      value.
    
    * ``auto_search``: a Boolean value, i.e., ``True`` or ``False``, 
      specifying whether or not to automatically determine the weighting 
      values and threshold value applying grid search strategy. If 
      ``True``, i.e., to use auto-search, then values given to 
      ``'w1'`` and ``'p'`` will be overridden.


