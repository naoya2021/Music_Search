from unicodedata import name
from django.urls import path,include
from django.urls.resolvers import URLPattern
from app import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import logout
# from django.views.generic.base import TemplateView
# from django.contrib.auth.decorators import login_required
# from accounts import views as accounts_views


app_name='app'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    # path('home/',views.IndexView.as_view(),name='index'),
    path('detail/<str:id>',views.DetailView.as_view(),name='detail'),
    path("", auth_views.LoginView.as_view(template_name="app/templates/login.html"), name="login"),
    path("login/", auth_views.LoginView.as_view(template_name="app/templates/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="app/templates/logout.html"), name="logout"),
    path('signup/', views.signup,name = 'signup'),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='passwprd_change_done'),
]