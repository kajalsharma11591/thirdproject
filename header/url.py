from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name='homepage'),
    path('about/', views.about,name='aboutpage'),
    path('con/', views.contact,name='contact'),
    path('dwn/', views.downloading,name='download'),
]


