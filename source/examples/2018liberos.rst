.. _examples_2018liberos:

###################################################################
Finding the "Liberos": Discover Organizational Models with Overlaps
###################################################################

This page presents a demo program used in a BPM 2018 paper [yang2018]_
for discovering groups with overlaps. Addressing this discovery task can
facilitate identifying generalist resources for process redesign.

This demo was originally hosted as a standalone program on a 
`GitHub repository <https://github.com/roy-jingyang/Org-Liberos>`_, where
the source code of the following demo now resides.

.. note::
   Before proceeding, make sure that *OrdinoR* has been installed.
   (:ref:`How to install? <install>`)

********
Download
********
Download and extract the bundled zip from 
`this link <https://github.com/roy-jingyang/Org-Liberos/archive/refs/heads/master.zip>`_,
in which you would find the following files:

.. code-block:: bash

    .
    ├── example_wabo_preprocessed.xes
    ├── LICENSE
    ├── main.py
    └── README.md

``main.py`` is the main program and ``example_wabo_preprocessed.xes`` 
provides an example event log sourced from 
`4TU.ResearchData <https://data.4tu.nl/repository/uuid:a07386a5-7be3-4367-9535-70bc9e77dbe6>`_,
preprocessed as described in Sect. 5.1 in the paper [yang2018]_.

***************
Run the Program
***************
Go to the working folder and run the program with the following command, 
with paths to the input and output specified accordingly.

.. code-block:: bash

    python main.py [<path_to_input_log_file>] [<path_to_output_result>]


Log files in the `IEEE XES <https://xes-standard.org/>`_ format are 
supported as input.

.. note::

    For a simple in-place help message on how to use the program

    .. code-block:: bash

        python main.py --help

The output file is formatted as shown below. Each row represents a 
discovered resource group, and member resource ids are separated by
semicolons:

.. code-block:: bash

    group,members
    0,member1;member2;...
    1,member3;member4;...
    ...

See below for an example.

******
A Demo
******
Go to the working folder and run the program with the following command

.. code-block:: bash

    python main.py example_wabo_preprocessed.xes wabo_org_model.txt

Then, follow the prompt to specify the method and configuration for 
discovering the organizational model as defined in the paper.

For instance, using method **MOC** with the desired number of groups set 
to **5**, we will obtain the discovery result saved in the file named 
``wabo_org_model.txt`` with contents like the following:

.. code-block:: bash

    group,members
    0,Resource06;Resource02;Resource04;Resource01;Resource03;Resource05;Resource07
    1,test;Resource19;Resource35;Resource33;Resource16;Resource11;Resource36;Resource14;Resource30;TEST;Resource31;Resource01;Resource40;Resource15;Resource38;admin3;Resource34;Resource27;Resource29;Resource37;Resource32;admin2;Resource24;Resource26;Resource08;Resource25
    2,Resource17;Resource18;Resource20;Resource21;Resource23;Resource09;Resource14;Resource12;Resource15;Resource16;Resource11;Resource13;Resource08;Resource22
    3,Resource28;admin2;Resource26;Resource09;Resource12;Resource25;admin1
    4,Resource10

*************
Report Issues
*************
Please use the `GitHub Issues page
<https://github.com/roy-jingyang/Org-Liberos/issues>`_.

