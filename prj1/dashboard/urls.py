from django.urls import path

from .views import HomeView, ConfirmedStatView, ConfirmedRegionView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]