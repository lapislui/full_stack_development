from django.urls import path
from first_app import views

app_name = 'first_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form_name_view, name='form_name_view'),
    path('users/', views.users, name='users'),
    path('userform/', views.userform, name='userform'),
    
]