Awesome Sphinx
==============

An automatically collected and curated list of Sphinx extensions, themes and other Sphinx-related projects.

.. hint:: 

   This documentation project is in an early phase and could need some love, smart ideas and beautiful designs from you.
   So why not join us on our `GitHub project <https://github.com/useblocks/awesomesphinx>`_?
   More details on our :ref:`contribute` page.


Featured themes and extensions
------------------------------

.. needextract::
   :filter: featured == "True"
   :layout: clean


All Extensions & Themes
-----------------------
To search for data in all table columns, simply use the search field on the upper right of the table.

Use the export buttons to get the current view as a PDF or Excel file.
The export takes filter and sorting into account.

.. needtable::
   :columns: id, title as "Name", content as "Description", sphinx_type as "Type", license, points, monthly as "Monthly downloads", release_days as "Days since last release"
   :colwidths: 10, 20, 35,10, 5, 5, 5, 10
   :style_row: awesome_[[copy('color')]]


Table of content
----------------

.. toctree:: 
   :caption: Packages
   :maxdepth: 2

   categories/extensions
   categories/themes
   categories/others

.. toctree::
   :caption: Analysis    
   :maxdepth: 2

   analysis/tags
   analysis/healthy
   analysis/famous
   analysis/active

.. toctree::       
   :caption: Collaboration
   :maxdepth: 2
   
   contribute 
   license
