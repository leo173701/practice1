from django.urls import path

# importing views from views..py
from .views import geeks_view, geeks2_view

urlpatterns = [
    path('geeks1/', geeks_view, name='geeks_view'),
    path('geeks2/', geeks2_view, name='geeks2_view')
]
