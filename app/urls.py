from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core.apis.views import get_users_api
from core.views import home, signup

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api-users/', get_users_api, name='api-users'),
    path('register/',signup, name='register'),
    path('', home, name='home'),

    # Interface Swagger Testando a API

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), 
        name='schema-swagger-ui'
    ),
]
