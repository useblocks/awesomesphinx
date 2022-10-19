.. awesome-sphinx documentation master file, created by
   sphinx-quickstart on Wed Oct 19 12:28:06 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Awesome Sphinx
==============

An automatically collectec and curated list of Sphinx extensions, themes and other Sphinx related projects.


All data
--------
.. needtable::
   :columns: id, title, sphinx_type, license, monthly, overall



Famous projects
---------------

Project with over 5.000 downloads per month

.. needtable::
   :filter: (int(monthly) if monthly.isdigit() else 0) >= 5000
   :columns: id, title, sphinx_type, license, monthly, overall


Analysis
--------

.. needpie:: Monthly downloads
   :labels: >50000,5000-49999, 1000-4999-,100-999,<100

   (int(monthly) if monthly.isdigit() else 0) >= 50000
   (int(monthly) if monthly.isdigit() else 0) < 50000 and (int(monthly) if monthly.isdigit() else 0) >= 5000
   (int(monthly) if monthly.isdigit() else 0) < 5000 and (int(monthly) if monthly.isdigit() else 0) >= 1000
   (int(monthly) if monthly.isdigit() else 0) < 1000 and (int(monthly) if monthly.isdigit() else 0) >= 100
   (int(monthly) if monthly.isdigit() else 0) < 100

Categories
----------

.. toctree:: 

   categories/others




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
