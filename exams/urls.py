from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^create_user/$', views.create_user, name='create_user'),
	url(r'^populate$', views.populate, name='populate'),
	url(r'^exam/(?P<date>\d+)/$', views.exam, name='exam'),
	url(r'^problem/(?P<pk>-?\d+)/$', views.problem, name='problem'),
	url(r'^advanced_search/$', views.advanced_search, name='advanced_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)