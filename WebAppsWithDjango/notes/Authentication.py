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
