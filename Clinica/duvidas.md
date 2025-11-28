## CTRL + ' OU CTRL + J -> abre o terminal
## python --version
## python -m venv venv
## .\venv\Scripts\activate
## pip install django
## django-admin startproject clinica .
## python manage.py runserver
## CTRL + C -> para parar o serviço/servidor do django
## CLS -> limpar a tela do terminal
## python manage.py startapp clientes
## pip install djangorestframework
## python manage.py makemigrations
## python manage.py migrate
## python manage.py runserver

## python manage.py startapp medicos
## crie/edite models
## crie/edite views
## crie/edite serializers
## Adicione no INTALLED_APPS = 'medico'
## Adicione a rota no urls de clinica
## from medicos.views import MedicoViewSet
## router.register(r'medicos', MedicoViewSet)

## python manage.py startapp paciente
## crie/edite models
## crie/edite views
## crie/edite serializers
## Adicione no INTALLED_APPS = 'paciente'
## Adicione a rota no urls de clinica
## from pacientes.views import PacienteViewSet
## router.register(r'pacientes', PacienteViewSet)

## adicionando os novos apps.
## python manage.py makemigrations
## python manage.py migrate
## python manage.py runserver

## python manage.py createsuperuser
## gustavoadm - 741852 (testes)