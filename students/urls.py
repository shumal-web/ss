from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name="students"),
    path('search/',views.search,name="search"),
]