from django.urls import path

from .views import HomeView, SearchView, StationView, AirDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('search/<str:key>', SearchView.as_view(), name='search'),
    path('stn/<str:key>', StationView.as_view(), name="stn"),
    path('detail/<str:key>', AirDetail.as_view(), name="detail"),
]