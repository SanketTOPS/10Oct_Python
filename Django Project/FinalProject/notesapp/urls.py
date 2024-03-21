from django.urls import path,include
from notesapp import views

urlpatterns = [
    path('',views.index),
]
