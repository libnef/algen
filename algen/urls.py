from django.db.utils import OperationalError
format_list = [('', '(all)')]
geom_type_list = [('', '(all)')]
try:
    format_list.extend([(i[0],i[0]) 
        for i in Format.objects.values_list('name')])
    geom_type_list.extend([(i[0],i[0]) 
        for i in Geom_type.objects.values_list('name')])
except OperationalError:
    pass  # happens when db doesn't exist yet, views.py should be
          # importable without this side effect
"""algen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('exams.urls')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}, name='logout'),
]