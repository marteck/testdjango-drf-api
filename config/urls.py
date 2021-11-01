"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-auth/', include('rest_framework.urls')),
    path('api/v1/', include('support.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    # api/auth/ password/reset/ [name='rest_password_reset']
    # api/auth/ password/reset/confirm/ [name='rest_password_reset_confirm']
    # api/auth/ login/ [name='rest_login']
    # api/auth/ logout/ [name='rest_logout']
    # api/auth/ user/ [name='rest_user_details']
    # api/auth/ password/change/ [name='rest_password_change']
    # api/auth/ token/verify/ [name='token_verify']
    # api/auth/ token/refresh/ [name='token_refresh']"""
    path('api/registration', include('dj_rest_auth.registration.urls')),

]

