from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('update',views.update,name = 'update'),
    path('login',views.login,name = 'login'),
    path('register',views.register,name = 'register'),
    path('display' , views.display,name = 'display'),
    path('match', views.match,name = 'match')
]