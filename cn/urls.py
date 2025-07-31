from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
        path('details/<int:news_id>/', views.details, name='details'),
   path('crud/', views.crud, name='crud'),
    path('crud/<int:pk>/', views.crud, name='crud_with_id'),

]
