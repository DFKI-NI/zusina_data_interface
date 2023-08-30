# ZuSiNa Datenschnittstelle

Im Forschungsprojekt ZuSiNa wurde eine Schnittstelle entwickelt, die zu Textilprodukten entsprechende Nachhaltigkeitssiegel ausgeben soll. Die Datenschnittstelle ist eine Rest API, die mit Django entwickelt wurde.

## Get started
Um die Schnittstelle zu implementieren muss das Django Framework installiert werden. Auf der Seite https://docs.djangoproject.com/en/4.2/intro/install/ wird beschrieben wie dies geht.

Mit Django kann dann eine REST API erstellt werden, dafür muss ein Django Projekt erstellt werden (https://docs.djangoproject.com/en/4.2/intro/tutorial01/) und es müssen einige Programme installiert werden.

```
pip install djangorestframework 
pip install django-filter  # Bibliothek zum erstellen von Filtern für die Daten
```

Das django Restframework muss zu den installierten Apps in der settings.py hinzugefügt werden

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'django_filters',
    'zusina_api',
    'rest_framework.authtoken',
]
```
Um später Authentifizierung zu ermöglichen fügen wir folgendes der settings.py hinzu:

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

Dem Projekt werden dann die Dateien 

```
models.py
serializer.py
views.py
admin.py
```

aus diesem Repo hinzugefügt.
Damit eine passende Datenbank hinzugefügt wird müssen folgende Kommandos verwendet werden:

```
python manage.py makemigrations <projektname>
python manage.py migrate
```





