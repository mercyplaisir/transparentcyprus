from django.urls import path
from . import views

urlpatterns =  [
    path('',views.default,name="views_homepage")
]