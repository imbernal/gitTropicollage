"""tropicollage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from tropicollage import settings
from rest_framework import routers
from app.views import *

router = routers.DefaultRouter()

router.register(r'casas', CasaViewSet)
router.register(r'galleries', GalleryViewSet)
router.register(r'images', ImagesViewSet)

urlpatterns = [
    url(r'^api/' , include(router.urls)),
    url(r'^api-auth/' , include('rest_framework.urls' , namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.home_page', name='home_page'),
    url(r'^$/contact', 'app.views.contact', name='contact'),
    url(r'^casas/$', 'app.views.homeList', name='casas'),
    url(r'^reservar/(?P<home_id>[0-9]+)$', 'app.views.reservar', name='reservar'),

    url(r'^casas/reservaciones/$', 'app.views.fecha_search', name='fecha_search'),
    url(r'^uploadData/$', 'app.views.uploadJson', name='upload_json'),
    url(r'^upload/$', 'app.views.upload', name='app_upload'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),

    url(r'^casas/detalles/(?P<home_id>[0-9]+)$', 'app.views.homeDetails', name='home_details'),
    url(r'^home_pictures/$', 'app.views.get_pictures_from_home', name='home_details'),
    # url(r'^list$', 'app.views.ax')
    url(r'^feedback/$', 'app.views.comment', name='comment'),
    url(r'^notif_mail/$', 'app.views.send_data', name='send_data')
]
