from django.urls import path
from . import views

urlpatterns = [
    # Lab #2
    path('list', views.list_post, name='list_post'),
    path('add', views.add_post, name='add_post'),
    
    # HW #1
    path('courselist', views.courselist, name='courselist'),
    path('addcourse', views.addcourse, name='addcourse'),
]