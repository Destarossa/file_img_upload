
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('upload/file/', views.upload_file, name='upload'),
    path('upload/img/', views.upload_img, name='img')

]
