from django.urls import path
from testapp import views

urlpatterns = [
    path('wish/', views.wish_view)
]