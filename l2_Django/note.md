# Create Django Project:
python3 -m startproject projectname
# Run Django Project
python3 manage.py runserver
# Create Django App:
python3 manage.py startapp appname

# Steps to follow:
1. Go to project settings.py, INSTALLED_APPS: add appname into the variables.
2. Go to app views.py def index(request): return HttpResponse("Hello, world!")
3. Create urls.py in app directory, and add things inside
4. Go to urls.py in project directory, add app urls inside