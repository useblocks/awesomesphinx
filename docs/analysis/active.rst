Active
======

.. needpie:: Days since last release
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
