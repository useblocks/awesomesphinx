Awesome Sphinx
==============

An automatically collected and curated list of Sphinx extensions, themes and other Sphinx related projects.

Featured themes and extensions
------------------------------

.. needextract::
   :filter: featured == "True"
   :layout: clean


All Extension & Themes
----------------------
To search for data in all table columns, simply use the search field on the upper right of the table.

Use the export buttons to get the current view as PDF or Excel file.
The export takes filter and sorting into account.

.. needtable::
   :columns: id, title as "Name", content as "Description", sphinx_type as "Type", license, points, monthly as "Monthly downloads", release_days as "Days since last release"
   :colwidths: 10, 20, 35,10, 5, 5, 5, 10
   :style_row: awesome_[[copy('color')]]


Project with most points
------------------------
.. needbar:: Quality points
   :show_top_sum:
   :xlabels: 0,1,2,3,4,5,6,7,8,9,10

   int(points) == 0, int(points) == 1,int(points) == 2,int(points) == 3,int(points) == 4,int(points) == 5,int(points) == 6,int(points) == 7,int(points) == 8,int(points) == 9,int(points) == 10

Projects with 9 points and higher.

.. needtable::
   :filter: int(points) >= 9
   :columns: id, title, sphinx_type, license, points, code_nice, pypi_nice, website_nice

Active project
--------------

.. needpie:: Days since last release_days
   :labels: <100, 100-199, 200-399, 400-799, >=800

   int(release_days) < 100
   int(release_days) >= 100 and int(release_days) < 200
   int(release_days) >= 200 and int(release_days) < 400
   int(release_days) >= 400 and int(release_days) < 800
   int(release_days) >= 800 

Projects with releases in the last 100 days

.. needtable::
   :filter: int(release_days) <= 100
   :sort: release_days
   :columns: id, title, sphinx_type, license, points, code_nice, pypi_nice, website_nice

Famous projects
---------------
.. needpie:: Monthly downloads
   :labels: >50000,5000-49999, 1000-4999-,100-999,<100

   (int(monthly) if monthly.isdigit() else 0) >= 50000
   (int(monthly) if monthly.isdigit() else 0) < 50000 and (int(monthly) if monthly.isdigit() else 0) >= 5000
   (int(monthly) if monthly.isdigit() else 0) < 5000 and (int(monthly) if monthly.isdigit() else 0) >= 1000
   (int(monthly) if monthly.isdigit() else 0) < 1000 and (int(monthly) if monthly.isdigit() else 0) >= 100
   (int(monthly) if monthly.isdigit() else 0) < 100

Projects with over 5.000 downloads per month

.. needtable::
   :filter: (int(monthly) if monthly.isdigit() else 0) >= 5000
   :sort: monthly
   :columns: id, title, sphinx_type, license, monthly, overall


Categories
----------

.. toctree:: 

   categories/extensions
   categories/themes
   categories/others
