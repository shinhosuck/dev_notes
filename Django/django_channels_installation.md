# django-channels installation

1. python -m pip install -U 'channels[daphne]'

2. INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    <!-- 3rd party app -->
    "daphne",
)

3. asgi.py:


    import os

    from channels.routing import ProtocolTypeRouter
    from django.core.asgi import get_asgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    # Initialize Django ASGI application early to ensure the AppRegistry
    # is populated before importing code that may import ORM models.
    django_asgi_app = get_asgi_application()

    application = ProtocolTypeRouter({
        "http": django_asgi_app,
        # Just HTTP for now. (We can add other protocols later.)
    })

4. settings.py

    ASGI_APPLICATION = "myproject.asgi.application"

    <!-- Only on development stage -->
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels.layers.InMemoryChannelLayer',
        }
    }
