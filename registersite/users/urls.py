from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<pk>/', views.detail, name='detail'),
    path('<pk>/delete/', views.delete, name='delete'),
]
