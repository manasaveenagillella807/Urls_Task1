"""
URL configuration for Movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from Devara.views import *
from Amaran.views import *
import pushpa
urlpatterns = [
    path('admin/', admin.site.urls),
    path('NTR/',NTR,name='NTR'),
    path('NTR2/',NTR2,name='NTR2'),
    path('Kartikeya/',Kartikeya,name='Kartikeya'),
    path('Kartikeya2/',Kartikeya2,name='Kartikeya2'),
    path('pushpa/',include('pushpa.urls')),
    path('Pushpa2/',include('Pushpa2.urls')),
]
