from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordChangeView

urlpatterns = [
    path('', views.index, name='index'),
        path('details/<int:news_id>/', views.details, name='details'),
   path('crud/', views.crud, name='crud'),
    path('crud/<int:pk>/', views.crud, name='crud_with_id'),
    path('articles/', views.all_articles_view, name='articles'),
    path('sports/', views.sports_news_view, name='sports'),
    path('login/', views.login_view, name='login'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('password-changed/', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_changed.html'
    ), name='password_change_done'),
]
