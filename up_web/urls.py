from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name=''),
    path('logout', views.logout_view, name='logout'),
    path('create_task', views.createTask, name='create_task'),
]
