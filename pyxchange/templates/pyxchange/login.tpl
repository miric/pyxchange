{% extends 'pyxchange/base_user.tpl' %}
{% block title %}Log In{% endblock %}

{% block body %}
  <div class="container">
    <div class="row text-center">
      <div class="col-md-4 col-md-offset-4 animated fadeInDown">
        <div class="panel panel-default">
          <div class="panel-body">
            <h3>Log In</h3>
            {% if error_message %}
              <p><b class="text-danger">{{ error_message }}</b></p>
            {% endif %}
            <form class="form-horizontal" role="form" action="{% url 'pyxchange:login_user' %}" method="post"
                  enctype="multipart/form-data">
              {% csrf_token %}
              <div class="form-group">
                <label class="control-label col-sm-2" for="id_username">Username:</label>
                <div class="col-sm-10">
                  <input id="id_username" maxlength="30" name="username" type="text">
                </div>
              </div>
              <div class="form-group">
                <label class="control-label col-sm-2" for="id_password">Password:</label>
                <div class="col-sm-10">
                  <input id="id_password" maxlength="30" name="password" type="password">
                </div>
              </div>
              <div class="form-group">
                <div class="col-md-4 col-md-offset-4">
                  <button type="submit" class="btn btn-success"><i class="fa fa-sign-in" aria-hidden="true"></i></span> Log In
                  </button>
                </div>
              </div>
            </form>
          </div>
          <div class="panel-footer">
            Don't have an account? <a href="{% url 'pyxchange:register' %}">Click here</a> to sign up.
          </div>
        </div>
      </div>
    </div>
  </div>
{% endblock %}
