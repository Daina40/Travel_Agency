from django.urls import path
from .views.tour_views import DestinationCreate, GuideCreate, TourPackageCreate
urlpatterns = [
    path('destination/', DestinationCreate.as_view(), name='destination'),
    path('guide/', GuideCreate.as_view(), name='guide'),
    path('tour_package/', TourPackageCreate.as_view(), name='tour_package'),
]