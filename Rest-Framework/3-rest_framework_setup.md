<!-- REST FRAMEWORK SETUP -->

1.  pip install djangorestframework

2.  INSTALLED_APPS = [
        'rest_framework',
         <!-- for token authentication -->
        'rest_framework.authtoken',
    ]

<!-- rest framework built in authenitcation panel -->
3.  urlpatterns = [
        path('api-auth/', include('rest_framework.urls'))
    ]

4.  REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            <!-- for token authentication -->
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.SessionAuthentication'
        ],
        'DEFAULT_PERMISSION_CLASSES': [
            # 'rest_framework.permissions.IsAuthenticated',
            # 'rest_framework.permissions.AllowAny',
            # 'rest_framework.permissions.IsAdminUser',
            'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ]
    }


<!-- CORS HEADERS SETUP -->

1.  python -m pip install django-cors-headers

2.  INSTALLED_APPS = [
        "corsheaders",
    ]

<!-- add CorsMiddleware above CommonMiddleware -->
3.  MIDDLEWARE = [
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
    ]

4.  CORS_ALLOWED_ORIGINS = [
        "http://127.0.0.1:3000",
    ]


<!-- JSON WEB TOKEN(JWT) -->
pip install djangorestframework-simplejwt

<!-- add to REST_FRAMEWORK -->
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}



<!-- ADD TO PROJECT URLS.PY -->
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


<!-- add to settings.py -->

INSTALLED_APPS = [
<!-- this needs to added to the apps if blacklist 'BLACKLIST_AFTER_ROTATION' is to set to true -->
        'rest_framework_simplejwt.token_blacklist',
]


from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False, # set to true
    "BLACKLIST_AFTER_ROTATION": False, # set to true
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

<!-- Decode Json Web Token -->
npm install jwt-decode
import jwt_decode from "jwt-decode"
var decoded = jwt_decode(token);
