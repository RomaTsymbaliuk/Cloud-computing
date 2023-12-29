from django.urls import path
from . import views


urlpatterns = [
    path('entries/update/<int:item_id>/', views.entry_update, name='entry_update'),
    path('entries/delete/<int:item_id>/', views.entry_delete, name='entry_delete'),
    path('entries/', views.entries, name='entries'),
    path('entries/add/', views.entry_add, name='entry_add'),
    path('entriezes/', views.get_data, name = "entriezes"),
    path('entries/api_post/', views.post_data, name = "post_data"),
    path('entries/api_get_by_time/', views.get_data_filter, name = "get_data_filter"),
    path('entries/api_get_by_purpose/', views.get_data_by_purpose, name = "get_data_by_purpose"),
    path('', views.entries, name='entries')
]