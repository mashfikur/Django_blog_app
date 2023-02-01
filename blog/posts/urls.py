from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('posts/<str:dynamic>',views.post,name='post')
]