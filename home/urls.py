from django.contrib import admin
from django.urls import path , re_path
from django.urls.conf import include
from home import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    path('', views.home, name="home"),
    path('search', views.search, name="search"),
    re_path(r'^download/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
    path('<str:slug>', views.download, name="download"),  
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)