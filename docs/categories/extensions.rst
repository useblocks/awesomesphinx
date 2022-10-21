Extensions
==========

Collected extensions for Sphinx.


.. This loads the analysis and data import for the category
   Set sphinx_type and table_columns to configure category specific stuff. 

{% set sphinx_type = "extension" %}
{% set table_columns = 'id, title, package_summary as "summary", license, points, code_nice as "Code", pypi_nice as "PyPi", website_nice as "Website"' %}
{% set col_width = "10, 15, 30, 10,5,10,10,10" %}

{% include '../_awesome_templates/analysis.rst' %}

{% include '../_awesome_templates/data_import.rst' %}

.. Add custom extensions below this line.

