from django.urls import path
from . import views


urlpatterns = [
    path('entries/update/<int:item_id>/', views.entry_update, name='entry_update'),
    path('entries/delete/<int:item_id>/', views.entry_delete, name='entry_delete'),
    path('entries/', views.entries, name='entries'),
    path('entries/add/', views.entry_add, name='entry_add'),
    path('entriezes/', views.main_method, name="entriezes"),
    path('entriezes/<int:item_id>/', views.main_method, name='entriezes'),
    path('', views.entries, name='entries')
]