{% extends 'pyxchange/base.tpl' %}
{% block title %}Upload a new image{% endblock %}

{% block body %}
    <form action="" method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {% include 'pyxchange/form-template.tpl' %}
        <button type="submit">Upload</button>
    </form>
{% endblock %}