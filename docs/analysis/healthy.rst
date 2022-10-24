Healthy
=======
AwesomeSphinx calculates a value to specify the health status of a project.
This health status is simple called `points`.

Points are given for downloads in the last month and time passed since the last release.
Both values are then added to an overall result.

The highest available amount of points is **10**, the lowest **0**.

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
   
.. needbar:: Health points
   :show_top_sum:
   :xlabels: 0,1,2,3,4,5,6,7,8,9,10

   int(points) == 0, int(points) == 1,int(points) == 2,int(points) == 3,int(points) == 4,int(points) == 5,int(points) == 6,int(points) == 7,int(points) == 8,int(points) == 9,int(points) == 10

Projects with 9 points and higher.

.. needtable::
   :filter: int(points) >= 9
   :columns: id, title, sphinx_type as "Type", package_summary as "Summary", points, download_points as "DL points", release_points as "Release points", code_nice as "Code Link", pypi_nice as "PyPi Link", website_nice as "Website Link"