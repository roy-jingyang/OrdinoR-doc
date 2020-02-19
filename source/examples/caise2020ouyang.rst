.. _examples_caise2020ouyang:

Discover and analyze organizational grouping
============================================

This page presents a demo program used in a paper submitted to CAiSE 
2020 (under review) [ouyang2020]_, for discovering organizational 
grouping from event logs, which then facilitates analysis of resource 
group behavior for the purpose of performance analysis.

This demo was originally a standalone program hosted on a 
`GitHub repository <https://github.com/roy-jingyang/caise-2020-Ouyang_Discovering>`_.

.. note::
   Before proceeding, make sure you have installed OrgMiner on your 
   machine. (:ref:`How to install? <install>`)

Replicate the experiments in the paper
--------------------------------------

Download and extract the bundled zip from 
`HERE <https://github.com/roy-jingyang/caise-2020-Ouyang_Discovering/archive/master.zip>`_,
in which you would find the following files:

.. code-block:: bash

    .
    ├── data
    │   └── BPIC15-decoded
    │       ├── BPIC15_1-decoded.csv
    │       ├── BPIC15_2-decoded.csv
    │       ├── BPIC15_3-decoded.csv
    │       ├── BPIC15_4-decoded.csv
    │       └── BPIC15_5-decoded.csv
    ├── main
    │   ├── analyze-bpic15_act-focused.py
    │   ├── analyze-bpic15_case-focused.py
    │   └── utilities.py
    └── README.md

Python scripts under folder ``main/`` are the main programs and in 
folder ``data/`` we provide the event logs necessary for replicating the 
experiments as reported in Sect. 5 in the paper [ouyang2020]_, sourced 
from `4TU.ResearchData <https://data.4tu.nl/repository/uuid:31a308ef-c844-48da-948c-305d167a0ec1>`_.

Appendix notes on the dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The description of the dataset shows the existence of certain 
hierarchical structure of process activities recorded in the event log, 
which is encoded by an event attribute named *action_code*. The whole 
building permit application handling process can thus be viewed as 
consisting of 21 subprocesses, among which there exists a main 
subprocess (indicated by the first two digits and the subsequent 
characters in the action code). Furthermore, a subprocess may be 
divided into several phases (suggested by the first digit immediately 
after the subprocess code segment), which then include the atomic 
activities that triggered the events (encoded by the remaining digits).

For example, an event with action code "01_HOOFD_010" in the log is 
corresponded with an activity "10" within the first phase "0" in the 
main subprocess "01_HOOFD". And an event with action code 
"01_HOOFD_015" should link to a following activity in the same trace.
For effective analysis, we considered each of the phases as an activity 
type in the experiments rather than directly using the activity labels. 
Under such view, the two events in the example above 
(with action codes "01_HOOFD_010" and "01_HOOFD_015") would have the 
same activity type ("01_HOOFD_0").

Case information is recorded in the log as case-level attributes, e.g. 
cost of the application, the last phase the application gone through. 
We selected attribute *last_phase* in this evaluation to distinguish 
among different categories of cases of the process.

Run the program
^^^^^^^^^^^^^^^
Open an `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_ 
(or the terminal for Unix-like systems), change to the root directory 
of the extracted files.

- For function-oriented grouping analysis, type

``python main/analyze-bpic15_act-focused.py data/BPIC15-decoded/BPIC15_1-decoded.csv ./``

and select ``k=3`` when prompted.

- For process-oriented grouping analysis, type

``python main/analyze-bpic15_case-focused.py data/BPIC15-decoded/BPIC15_1-decoded.csv ./``

and select ``k=4`` when prompted.

Running either of two commands would generate the results and output 4 
separated CSV format files under the current folder:

* ``profiles.csv``, resource profiles annotated with their group labels.
* ``group-profiles.csv``, group profiles derived on the basis of 
  resource profiles.
* ``time-avg.csv`` and ``time-full-info.csv``, used for performance 
  analysis (cf. Sect. 5.1 & 5.3 in the paper).

Analyze other event logs
^^^^^^^^^^^^^^^^^^^^^^^^
You may play it around with other 4 event logs in the BPIC2015 
dataset provided, which can be found under folder ``data``.

Note that event log files provided here were converted from the original 
event log data to CSV format, with two columns appended which contain 
the information extracted from the field "action_code". However, no 
modification on the original data was made.

You can edit the program code to adjust some of the parameter:

* Event/Case filtering options: modify the parameters of the filtering
  functions by referring to the comments in the main program code and 
  also those in ``main/utilities.py``.
* Methods for building resource profiles: adjust the parameter of 
  function ``count_execution_frequency``, with ``scale=None`` the 
  count of frequency is used; with ``scale=normalize`` the load 
  distribution is used.

