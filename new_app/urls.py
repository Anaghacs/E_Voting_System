from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('login',views.login,name="login"),
    path('user_login',views.user_login,name="user_login"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('user_home',views.user_home,name="user_home"),
    path('view_users',views.view_users,name="views_users"),
    path('delete/<int:id>/',views.delete,name="delete")

    # path('vote',views.vote,name="vote"),


]