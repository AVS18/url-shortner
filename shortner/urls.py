from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('addlink',views.addlink,name="addlink"),
    path('mylink',views.mylink,name='mylink'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('link/<str:id>',views.redirector,name="redirector")
]
