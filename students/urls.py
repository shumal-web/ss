from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name="students"),
    path('racks/',views.racks,name="racks"),
    path('search/',views.search,name="search"),
    path('rackResult/',views.rckres,name="rck_res"),
]