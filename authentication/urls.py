from django.urls import path

from authentication.views import *

urlpatterns = [
    path("login", Login.as_view(),{"bla":"bla"}),
    path("logout", Logout.as_view()),
    path("usersignup", UserSignup.as_view()),
    path("authorsignup",AuthorSignup.as_view()),
    path("adminsignup",AdminSignup.as_view()),
    path("changepassword", ChangePassword.as_view())
]