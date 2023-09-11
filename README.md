# ZuSiNa Datenschnittstelle

Im Forschungsprojekt ZuSiNa wurde eine Schnittstelle entwickelt, die zu Textilprodukten entsprechende Nachhaltigkeitssiegel ausgeben soll. Die Datenschnittstelle ist eine Rest API, die mit Django entwickelt wurde.

## Installation
Um die Schnittstelle zu implementieren muss das Django Framework installiert werden. Auf der Seite https://docs.djangoproject.com/en/4.2/intro/install/ wird beschrieben wie dies geht.

Mit Django kann dann eine REST API erstellt werden, dafür muss ein Django Projekt erstellt werden 
```
django-admin startproject zusina_api
```

 und es müssen einige Programme installiert werden, die in der requirements.txt zu finden sind.

## Implementation
In dem Projektordner zusina_api müsste eine Datei namens manage.py und ein Ordner zusina_api sein. 
In dem Ordner zusina_api befindet sich die Datei settings.py in die wir nun folgendes einfügen:

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'django_filters',
    'zusina_api',
    'rest_framework.authtoken',
]
```
Um später Authentifizierung zu ermöglichen fügen wir folgendes ebenfalls der settings.py hinzu:

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

Dem Projekt werden dann die Dateien aus diesem Repo hinzugefügt. Diese kommen in den selben Ordner wie settings.py.

```
models.py
serializer.py
views.py
admin.py
```

Damit eine passende Datenbank hinzugefügt wird müssen folgende Kommandos verwendet werden:

```
python manage.py makemigrations <projektname>
python manage.py migrate
```
Es sollte noch ein superuser hinzugefügt werden, um auf die Datenbanken über /admin zuzugreifen.

```
python manage.py createsuperuser --username <superusername>
```

Bevor die Schnittstelle aufgerufen werden kann müssen noch die Adressen registriert werden. Dies geschieht durch hinzufügen der folgenden Zeilen zu der Datei urls.py.

```
...
from zusina_api.views import ProductAPIView, ProductDetailAPIView

urlpatterns = [
    ...
    path('api/', ProductAPIView.as_view()),
    path('api/alldata', ProductDetailAPIView.as_view()),
]
```

Danach kann der Server gestartet werden.

```
python manage.py runserver
```

## Verwendung

## Förderung
Die Dateien in diesem Repository wurden im Rahmen des Forschungsprojekts ZuSiNa, das vom Bundesministerium für Umwelt, Naturschutz, nukleare Sicherheit und Verbraucherschutz (BMUV) gefördert wird (FKZ: 67KI21009A) vom DFKI entwickelt. An dem ersten Arbeitspaket, in dem diese Dateien entwickelt wurden, sind die Institute ConPolicy (Leitung von AP1), Fraunhofer CERRI und DFKI beteiligt. Weitere Informationen sind auf https://www.zusina-projekt.de/ zu finden. 






