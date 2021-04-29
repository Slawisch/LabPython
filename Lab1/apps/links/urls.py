from django.urls import path
from . import views
from Lab1 import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'media'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:link_id>/', views.detail, name='detail'),
    path('<int:link_id>/addLikeDislike/', views.addLikeDislike, name='addLikeDislike'),
]
