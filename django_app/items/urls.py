from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('add/', views.add_item, name='add_item'),
    path('flask-message/', views.get_flask_message, name='flask_message'),  # 👈 add this line
]