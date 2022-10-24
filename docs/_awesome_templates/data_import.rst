{#
Template for all category-specific data imports

Do not add any category-specific configuration here.
Instead make it configurable by variables, like sphinx_type.
#}


Data
----

.. needimport:: {{need_ipmort_file}}
   :filter: sphinx_type == "{{sphinx_type}}"
