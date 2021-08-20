.. OrdinoR documentation master file, created by
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

#####################
OrdinoR Documentation
#####################

.. hint::

   *Ordino: "to organize"; R: "resources"*

*OrdinoR* is a Python_ toolkit for organizational model mining, built
upon our recent research and capable of supporting the discovery,
evaluation, and analysis of organizational models based on event logs. 
It addresses several critical gaps in the academic literature on the
topic, and opens up many possibilities for future research as well as
applications, for example, conformance checking of organizational models.

**********
Background
**********
Successful human resource management plays a crucial part in building
organizational effectiveness, which relies on decision-makers
understanding how their employees act in groups to achieve organizational
outcomes.
Building this essential HR capability requires seasoned expertise of
managers, empowered by the presence of accurate and timely information
about the workforce.

Process mining [vdaalst2016]_ offers useful tools to derive
organizational models [song2008]_ (from business process execution data
(notably in the form of event logs). 
These models can capture workforce-related knowledge and provide
organizations with insights into their structures and staff deployment.

**********
How to Use
**********

You can find the :ref:`installation guide <install>` and several 
:ref:`examples <examples_index>` from our research work based on *OrdinoR* 
(or its `earlier version <https://orgminer.readthedocs.io>`_).

*OrdinoR* can be used in two ways.

Using the example applications
==============================
You are welcome to use the programs and tools developed as part of our
research outcomes. For instance, "Arya" is a webapp providing a graphical
interface to perform organizational model mining with *OrdinoR*. 
There are also command-line programs developed mainly for the purpose of
conducting experiments in our research. 

For more information on what's available and how to use the applications,
please visit :ref:`examples_index`.

Developing new applications
===========================
The *OrdinoR* library is built to be extensible. Users are welcome to
develop their own approaches for organizational model mining, either
through configuring the examples provided, or through creating new
methods/modules that extend the *OrdinoR* library.

We are currently working on a structured reference to the API.


*****************
How to Contribute
*****************
We welcome further contributions to this project. Please feel free to
Email_ us or find us on GitHub_.


*********************
Licensing Information
*********************
The `GNU GPLv3 license <https://www.gnu.org/licenses/gpl-3.0.en.html>`_ 
applies to the *OrdinoR* project.


****************
Related Software
****************

* Process Mining for Python: `PM4Py`_
* Process mining software: `Fluxicon Disco`_
* Python Data Analysis Library: `Pandas`_
* Software for complex networks: `NetworkX`_


.. _Python: https://www.python.org/
.. _license: https://www.gnu.org/licenses/gpl-3.0.en.html
.. _PM4Py: https://pm4py.fit.fraunhofer.de/
.. _Fluxicon Disco: https://fluxicon.com/disco/
.. _Pandas: https://pandas.pydata.org/
.. _NetworkX: https://networkx.github.io/

.. _Email: mailto:roy.j.yang@qut.edu.au
.. _GitHub: https://github.com/roy-jingyang/OrdinoR
