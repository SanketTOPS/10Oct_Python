from django.urls import path,include
from notesapp import views

urlpatterns = [
    path('',views.index),
    path('notes/',views.notes,name='notes'),
    path('about/',views.about),
    path('contact/',views.contact),
    path('profile/',views.profile),
    path('userlogout/',views.userlogout),
]
