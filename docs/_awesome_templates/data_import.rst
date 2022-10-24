{#
Template for all category-specific data imports

Do not add any category-specific configuration here.
Instead make it configurable by variables, like sphinx_type.
#}


Data
----

.. needimport:: /../data/20221024_awesome.json
   :filter: sphinx_type == "{{sphinx_type}}"
