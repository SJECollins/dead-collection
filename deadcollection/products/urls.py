from django.urls import path, include
from . import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view())
]