from django.contrib import admin
from django.urls import path, include
from items.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('items.urls')),  # 👈 This line connects your app-level urls
    path('', home),  # root route
]



   