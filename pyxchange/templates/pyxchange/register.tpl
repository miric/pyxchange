{% extends 'pyxchange/base.tpl' %}
{% block title %}Pyxchange User Register{% endblock %}

{% block body %}
    <h3>Create a New Account</h3>
    <form action="" method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {% include 'pyxchange/form_template.tpl' %}
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
                <button type="submit" class="btn btn-success">Submit</button>
            </div>
        </div>
    </form>
    <div class="col-sm-offset-2 col-sm-10">
        <hr />
        {% for pict in images %}
            <a href="{% url 'pyxchange:detail' pict.slug %}"><img src="{{ pict.img.url }}" width="100" alt="{{ pict.desc }}" title="{{ pict.desc }}" /></a>
        {% endfor %}
    </div>
{% endblock %}