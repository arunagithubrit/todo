from django.urls import path
from taskapi import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('v1/todos',views.TodosViewSetView,basename='v1todos')
router.register('v2/todos',views.TodoModelViewSetView,basename='v2todos')
urlpatterns=[
    
]+router.urls
