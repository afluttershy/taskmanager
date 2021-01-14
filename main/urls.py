from django.urls import path, re_path, include
from . import views
from rest_framework import routers
from .views import TaskViewSet
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('delete/<int:id>/', views.delete),
    path('edit/<int:id>/', views.edit),
    path('gettasks', views.gettasks)

]
