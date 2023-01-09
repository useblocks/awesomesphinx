Famous
======

.. needpie:: Monthly downloads
   :labels: >50000,5000-49999, 1000-4999,100-999,<100

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