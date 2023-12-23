from django.urls import path
from . import views


urlpatterns = [
    path('entries/delete/<int:item_id>/', views.entry_delete, name='entry_delete'),
    path('entries/', views.entries, name='entries'),
    path('entries/add/', views.entry_add, name='entry_add'),
]
