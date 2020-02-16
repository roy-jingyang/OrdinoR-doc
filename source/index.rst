.. OrgMiner documentation master file, created by
   sphinx-quickstart on Fri Dec 13 15:16:25 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _contents:

********
OrgMiner
********

Overview
========
OrgMiner: tookit for Process Mining on the organizational perspective

Process mining is an emerging discipline that bridges the gap between 
traditional process science (e.g., simulation-based business process 
analysis) and the rapidly-growing data science research (e.g., machine 
learning on big data), which offers a comprehensive set of tools to 
provide fact-based insights supporting business process improvement 
[vdaalst2016]_.

Whereas lion's share of research in process mining has been devoted to 
the control-flow perspective of business processes, event log data may 
also contain a wealth of information related to other pespectives. 
Organizational perspective concerns human resources related to a 
process, especially the ones as participants in process execution. 
Impact of human resource behavior on process execution has been 
recognized by many literature [song2008]_, making process mining 
research on the organizational perspective both interesting and 
valuable. Outcomes from this branch of process mining research, known 
as organizational mining, are expected to support process owners and 
business analysts in gaining accurate and timely understandings of the 
organizational settings (e.g., group structure, coordination) related 
to their end-to-end business processes, and to further assist in 
decision-making regarding human resources.

The current release of OrgMiner is based on our recent research progress 
reported in a preprint paper submitted to the journal of Information 
Systems. The library includes all the necessary modules and functions to 
implement the approach proposed in the paper and thus enables 
replicating the designed experiments for evaluation.

Process Mining
--------------

Licensing information
---------------------
The GNU GPLv3 license applies for artifacts of this project.

Documentation
-------------

.. only:: html

    :Release: |version|

.. toctree::
   :maxdepth: 1

   install
   tutorial
   reference/index
   auto_examples/index
   license
   credits
   citing
   bibliography

Indices and tables
------------------
* :ref:`modindex`

Related Softwares
-----------------
* pm4py
* ProM
* Disco
* pandas
* NetworkX

References
----------
.. [vdaalst2016] Van der Aalst, W. M. P. (2016). Process Mining: Data Science in Action (2nd ed.). Springer.
.. [song2008] Song, M., & van der Aalst, W. M. P. (2008). Towards comprehensive support for organizational mining. Decision Support Systems, 46(1), 300–317.
