from django.urls import path

from core.views import *

urlpatterns = [
    path("keyword", KeywordCrud.as_view(), {"bla": "bla"}),
]
