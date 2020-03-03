.. OrgMiner documentation master file, created by
   sphinx-quickstart on Fri Dec 13 15:16:25 2019.
   You can adapt this file completely to your liking, but it should at 
   least contain the root `toctree` directive.

.. toctree::
   :maxdepth: 1
   :hidden:

   install
   examples/index
   citing
   bib

.. _index:

********************
Overview of OrgMiner
********************
OrgMiner: Python tookit for Process Mining on the organizational 
perspective

*Process mining* is an emerging discipline that bridges the gap between 
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
research on the *organizational perspective* both interesting and 
valuable. Outcomes from this branch of process mining research, known 
as organizational mining, are expected to support process owners and 
business analysts in gaining accurate and timely understandings of the 
organizational settings (e.g., group structure, coordination) related 
to their end-to-end business processes, and to further assist in 
decision-making regarding human resources.

*OrgMiner* is developed as a Python_ library that aims at providing a 
toolkit for research and applications on the topic of organizational 
mining. The current focus targets the issue of organization model 
mining, which concerns the structuring of human resources into groups 
and how it is related with business processes.

The current release of OrgMiner is based on our recent research progress 
reported in a preprint paper [yang2020]_  submitted to the journal 
of Information Systems. The library includes all the necessary modules 
and functions to implement the approach proposed in the paper and thus 
enables replicating the designed experiments for evaluation.

Licensing information
=====================
The GNU GPLv3 license_ applies for artifacts of the OrgMiner project.

How to Use
==========
To get started, OrgMiner needs to be installed on your machine. See 
:ref:`install` for a step-by-step guide.

OrgMiner could be used in two ways:

* **through existed applications**

You are welcome to be a user of the developed main programs either 
with a simple graphical interface, e.g., the prototype for producing 
the visualization in the paper, or those interacted via 
command-line. See :ref:`examples_index` for detailed introduction of 
these available options as well as instructions on how to run them.

* **through developing new applications**

This library is established such that it allows a user to 
build their own approaches for organizational model discovery and 
conformance checking, either by adjusting and extending the existed 
methods, or by inventing new methods/modules that extend the library. 
We are currently working on a structured references on how to do this. 
For now a starting point could be modifying the existed programs and 
adjust the parameters to your liking.

Further contributions to this project are welcomed.
Email_ us or find us on GitHub_.

Related Software
================
* Process Mining for Python: pm4py_
* Process mining software: Disco_
* Python Data Analysis Library: pandas_
* Software for complex networks: NetworkX_


.. _Python: https://www.python.org/
.. _license: https://www.gnu.org/licenses/gpl-3.0.en.html
.. _pm4py: https://pm4py.fit.fraunhofer.de/
.. _Disco: https://fluxicon.com/disco/
.. _pandas: https://pandas.pydata.org/
.. _NetworkX: https://networkx.github.io/

.. _Email: mailto:roy.j.yang@qut.edu.au
.. _GitHub: https://github.com/roy-jingyang/OrgMiner


