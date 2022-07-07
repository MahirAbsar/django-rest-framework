from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name="home"),
    path('stu_obj/<str:id>',views.stu_obj,name="stu_obj"),
    path('stu_list/',views.stu_list,name="stu_list")

]
