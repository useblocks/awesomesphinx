Tags
====

{% for tag, desc in project_tags.items() %}
{{tag}}
{{"-" * tag|length}}

{{desc}}

.. needtable:: 
   :filter: "{{tag}}" in tags
   :columns: id; title; package_summary
   :colwidths: 10, 30, 60

.. needextract:: 
   :filter: "{{tag}}" in tags


{% endfor %}