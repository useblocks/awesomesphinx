{% for tag, desc in project_tags.items()|sort() %}
.. _tag_{{tag}}:

{{tag|capitalize}}
{{"=" * tag|length}}

{{desc}}

.. needtable:: 
   :filter: "{{tag}}" in tags
   :columns: id; title; package_summary
   :colwidths: 10, 30, 60


.. dropdown:: Element details
   :animate: fade-in

   .. needextract:: 
      :filter: "{{tag}}" in tags


{% endfor %}