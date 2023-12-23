from django.urls import path
from . import views

urlpatterns = [
    path('entries/', views.entries, name='entries'),
    path('entries/add/', views.entry_add, name='entry_add')
]
