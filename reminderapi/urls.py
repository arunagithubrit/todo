from django.urls import path
from reminderapi import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("v4/todos",views.TodosViewsetView,basename="v4todos")

urlpatterns=[
    path("v3/signup/",views.UserCreationView.as_view())
]+router.urls