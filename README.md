# SoftwareQualityEngineeringAssignment
Assignment project XSS DHBW CAS WiSe22-23

## django webapp with xss fuzzer
This Django webapp projcet tests cross-site scripting vulnerabilities using the xss fuzzer.

## run tests
1. python 3.x
2. py -m venv _venv
3. activate
4. install requirements.txt
5. py -m pytest tests/ --driver Chrome --driver-path <path> -rs -vv

## django setup with one app
1. python 3.x
2. mkdir root -> cd root
3. py -m venv _venv
4. activate
5. install requirements.txt
6. mkdir django -> cd django
7. django-admin startproject mysite
8. cd mysite
9. mkdir apps -> cd apps -> mkdir demo_app
10. python manage.py startapp demo_app apps/demo_app
11. add route in mysite.urls -> path('demo',include('apps.demo_app.urls'))
12. add route in apps.demo_app.urls ->  path('', views.index, name='index')
13. add view in apps.demo_app.views def index(request):return HttpResponse("Hello, world. You're at the demo_app index.")
13. test run -> python manage.py runserver

## django setup db
1. python manage.py migrate
2. Create model in  apps.demo_app.models
3. Change apps.demo_app.app -> DemoAppConfig(AppConfig): name = 'apps.demo_app'
3. Add mysite/settings.py -> INSTALLED_APPS = ['apps.demo_app' ...
4. python manage.py makemigrations demo_app
5. python manage.py migrate
6. python manage.py createsuperuser
7. test run -> python manage.py runserver
