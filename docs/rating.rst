Rating
======

AwesomeSphinx calculates a value to specify the health status of a project.
This health status is simple called `points`.

Points are given for downloads in the last month and time passed since the last release.
Both values are then added to an overall result.

The highest available amount of points is **10**, the lowest **0**.

Release day rating
------------------

The latest release day if taken from PyPI, by analysing the release day of each release and taking the latest one.

Points for release days:

.. list-table:: 

   - * Requirement
     * Points
   - * < 100
     * 5 
   - * < 200
     * 4 
   - * < 400
     * 3 
   - * < 600
     * 2 
   - * >= 600
     * 0 

Download rating
---------------

The download numbers are taken from the BigQuery Table from PyPI.
The data is stored on Google cloud and querying >1TB per month costs money, these numbers get updated once a week.


Points for monthly downloads:

.. list-table:: 

   - * Requirement
     * Points
   - * > 50.000
     * 5 
   - * > 5.000
     * 4 
   - * > 1.000
     * 3
   - * > 500
     * 2
   - * > 100
     * 1
   - * <= 100
     * 0