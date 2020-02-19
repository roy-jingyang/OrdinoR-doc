.. _examples_bpm2018yang:

Discover organizational groups with overlaps
============================================

This page presents a demo program used in a paper accepted and published 
in the conference proceedings of BPM 2018 [yang2018]_, 
for discovering models (groups) with overlaps, which may then facilitate 
the identification of generalist resources for process redesign.

This demo was originally a standalone program hosted on a 
`GitHub repository <https://github.com/roy-jingyang/bpm-2018-Yang_Find>`_.

.. note::
   Before proceeding, make sure you have installed OrgMiner on your 
   machine. (:ref:`How to install? <install>`)

How to Use
----------

Download and extract the bundled zip from 
`HERE <https://github.com/roy-jingyang/bpm-2018-Yang_Find/archive/master.zip>`_,
in which you would find the following files:

.. code-block:: bash

    .
    ├── example_wabo_preprocessed.xes
    ├── main.py
    └── README.md

``main.py`` is the main program and ``example_wabo_preprocessed.xes`` 
provides an example event log sourced from 
`4TU.ResearchData <https://data.4tu.nl/repository/uuid:a07386a5-7be3-4367-9535-70bc9e77dbe6>`_,
preprocessed as described in Sect. 5.1 in the paper [yang2018]_.

Run the program
^^^^^^^^^^^^^^^
Open an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_ 
(or the terminal for Unix-like systems), change to the root directory 
of the extracted files (or move the main program to whichever folder you 
like), and run the program with the following command:

``python main.py [path_to_input_log_file] [path_to_output_result]``

by specifying paths to the input and output accordingly.

Log files of `IEEE XES <https://xes-standard.org/>`_ format are 
supported as input.

The output files are formatted as follows, with each row representing a 
discovered resource group. For each row, member resource ids are 
separated by commas:

.. code-block:: bash

    group;members
    0;member1,member2,...
    1;member3,member4,...
    ...

See below for an example.

Run on the example log file
^^^^^^^^^^^^^^^^^^^^^^^^^^^
In Anaconda Prompt (terminal), change to the root directory of the 
extracted files, and enter

``python main.py example_wabo_preprocessed.xes wabo_org_model.txt``

and then follow the prompt to specify the method and configuration for 
discovering the organizational model as defined in the paper. Note that 
4 methods are available which are shown in the experiment section.

For instance, using method **MOC** with the desired number of groups set 
to **5**, we will obtain the discovery result saved in the file named 
``wabo_org_model.txt`` with contents:

.. code-block:: bash

    group;members
    0;Resource06,Resource02,Resource05,Resource04,Resource03,Resource01,Resource07
    1;Resource31,Resource25,admin3,TEST,Resource11,Resource16,Resource36,Resource34,Resource19,Resource30,admin2,Resource29,Resource33,Resource38,Resource26,Resource32,Resource15,Resource24,Resource08,Resource01,Resource27,test,Resource37,Resource14,Resource35,Resource40
    2;Resource13,Resource21,Resource17,Resource15,Resource22,Resource08,Resource11,Resource09,Resource20,Resource16,Resource14,Resource12,Resource18,Resource23
    3;Resource09,admin1,Resource25,Resource28,Resource26,Resource12,admin2
    4;Resource10

