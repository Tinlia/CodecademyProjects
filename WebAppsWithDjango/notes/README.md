# Notes
A collection of notes taken from Codecademy's `Build Python Web Apps With Django` course.

# Introduction

# Templates

# Data and Models

# Views

# Forms

# Accounts and Authentication

## The authenticate() Method
```python
from django.contrib.auth import authenticate

def login_view(request):
  # Both username and password are captured from the submitted log in form
  username = request.POST["username"]
  password = request.POST["password"]

  # Both username and password are passed into the authenticate() method to verify the user
  user = authenticate(request, username=username, password=password)
 
  # If the user is valid, then a user object is returned.
  if user is not None:
    # Log in user and redirect them
    return redirect("home.html")
  else:
    return HttpResponse("Invalid credentials!")
```

## Logging in
```HTML

{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'vetoffice/style.css' %}">

<h2>Please login</h2>
<form class="login" method="post">
  <div>
    {% csrf_token %}
    <!-- Add your form.as_p method below -->
    {{ form.as_p }}
    <input type="submit" value="Login"/>
  </div>
</form>

```
