{#
Template for for all category analysis.

Do not add any category specific configuration here.
Instead make it configurable by variables, like sphinx_type.
#}

Overview
--------

.. needtable::
   :filter: sphinx_type == "{{sphinx_type}}"
   :columns: {{table_columns}}
   {% if col_width is defined -%}
   :colwidths: {{col_width}}
   {%- endif %}

