from django.urls import path

from  administrator.views import *

urlpatterns = [
    path("update-author-status/<str:id>", UpdateAuthorStatus.as_view(),{"bla":"bla"}),

]