.. _examples_infsyst2020yang-common:

"OrgMining 2.0": organizational model mining framework
======================================================

This page presents the usage of several example programs used for the 
discovery and conformance checking of organizational models [yang2020]_.

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
    ├── LICENSE
    ├── main
    │   ├── om_discover.py
    │   ├── om_evaluate.py
    │   └── om_toy_test.py
    ├── README.md
    └── tools
        ├── analyze_log.py
        └── annotate_by_split_logs.py

The ``experiment/`` folder contains the necessary files for replicating 
the major part of the experiments. See :ref:`examples_infsyst2020yang-replicate` 
for more information.

The ``main/`` folder contains the main programs interacted via Command-Line 
Interface, and ``tools/`` contains some utility programs. See below for 
the usage of all these programs, respectively.

.. _examples_infsyst2020yang-common_discover:

Discover an organizational model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_ 
(or the terminal for Unix-like systems), change to the ``main/`` 
directory (or move the main program to whichever folder you like as 
workspace). 

.. note::

    For a simple help message on how to use the program in-place, type:
    ``python om_discovery.py --help``

To discover an organizational model from a given event log, run the 
following command:

``python om_discover.py [path_to_input_log_file] [path_to_output_model_file]``

with paths to the input and output specified accordingly.

Log files of `IEEE XES <https://xes-standard.org/>`_ format are 
supported as input.

As outputs, the fitness and precision values of a discovered 
organizational model will be printed on screen.

2 files will be generated and can be found via the output path 
specified:

organizational model
    Output organizational models are stored in formatted texts, as shown 
    in the example below. Each row represents a resource group, with a 
    group id as integer, group member ids (separated by semicolons), and 
    group capabilities (separated by semicolons). For each capability 
    (i.e., execution mode) of a resource group, its corresponding case 
    type, activity type and time type are separated by a vertical bar 
    ``|``.

.. code-block:: bash

    0,Bob;Pete,VIP|register|morning;normal|register|afternoon
    1,John;Sue,normal|check|morning;normal|decide|morning
    2,Mary,VIP|check|afternoon;VIP|decide|afternoon
    3,Ann,normal|contact|afternoon

(mappings) of collection of execution modes
    Mappings showing how the derived execution modes correspond to the 
    original event log data.p
    Exported mappings will be stored in a file, of which the name will 
    be specified as appending **".mode_mappings"** after the output 
    model file name specified by the user.


Check the conformance of an organizational model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_ 
(or the terminal for Unix-like systems), change to the ``main/`` 
directory (or move the main program to whichever folder you like as 
workspace).

.. note::

    For a simple help message on how to use the program in-place, type:
    ``python om_evaluate.py --help``

To check the conformance of an organizational model with a given event 
log, run the following command:

``python om_evaluate.py [path_to_input_log_file] [path_to_input_mode_mappings] [path_to_input_model_file]``

with paths to the inputs specified accordingly.

Log files of `IEEE XES <https://xes-standard.org/>`_ format are 
supported as input.

As outputs, the fitness and precision values of the given organizational 
model with respect to the given event log will be printed on screen.


Test the "toy" model
^^^^^^^^^^^^^^^^^^^^
A main program is also provided for testing the "toy" organizational 
model used in Sect. 3 of the paper (for which Figure 3 presents **part 
of the visualization** of it). Full details of the toy model are as 
shown below:

.. code-block:: bash

    0,Bob;Pete,VIP|register|morning;normal|register|afternoon
    1,John;Sue,normal|check|morning;normal|decide|morning
    2,Mary,VIP|check|afternoon;VIP|decide|afternoon
    3,Ann,normal|contact|afternoon

Run the program ``main/om_toy_test.py`` will reproduce this toy model, 
and calculate all the conformance checking measures presented in Sect. 
3.5, then print the values on screen. To do so, open an 
`Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_ 
(or the terminal for Unix-like systems), change to the ``main/`` 
directory (or move the main program to whichever folder you like as 
workspace), type

``python om_toy_test.py``

As output, a file named ``toy_example.om`` will be generated.


Notes on the tool programs
^^^^^^^^^^^^^^^^^^^^^^^^^^
The following shows a brief introduction on the utility programs stored 
under ``tools/`` folder.

.. code-block:: bash

    .
    ├── analyze_log.py
    └── annotate_by_split_logs.py

``analyze_log.py`` can be used to obtain some statistics of a given 
event log in `IEEE XES <https://xes-standard.org/>`_ format. Open an 
Anaconda Prompt (or terminal), type

``python analyze_log.py [path_to_input_log_file]``

Feel free to modify the code and play around with log data. Note that an 
event log is imported as a Pandas DataFrame 
(`What is it? <https://www.geeksforgeeks.org/python-pandas-dataframe/>`_).

``annotate_by_split_logs.py`` can be used to generate a "report" of 
trace clustering results from the outputs of "Guide Tree Miner" plugin
[bose2009]_ in 
`ProM 6 <http://www.promtools.org/doku.php>`_, which are a set of logs 
produced from applying trace clustering on a source log). 
Generated "report" files used for performing 
:ref:`organizational model discovery <examples_infsyst2020yang-common_discover>`, 
when method **"CT+AT+TT (trace clustering)"** is selected and a trace 
clustering report file is required as additional input.

To use the tool,

1. Generate the trace clustering results using ProM 6
2. Export the obtained split log files under a folder
3. In your Anaconda Prompt (or terminal), type

``python annotate_by_split_logs.py [path_to_the_folder]``

all log files with file type ".xes" will be recognized and combined, and 
the corresponding report will be saved in a file named 
``trace_clustering.result``, which can then be used for performing model 
discovery using **"CT+AT+TT (trace clustering)"**.


