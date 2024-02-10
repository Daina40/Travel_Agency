from rest_framework import serializers
from apps.tour_package.models import DestinationModel, GuideModel, TourPackageModel


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationModel
        fields = ['destination_name', 'location', 'description']

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideModel
        fields = ['guide_name', 'expirence', 'destination', 'person_photo', 'nid_frontside_img', 'nid_backside_img']

class TourPackageSerializer(serializers.ModelSerializer):
    class Meta:
        starting_time_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
        ending_time_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
        bus_start = serializers.TimeField(format="%H:%M:%S")
        model = TourPackageModel
        fields = ['title', 'guide', 'starting_time_date', 'ending_time_date', 'total_seat', 'seat_booking_number', 'bus_start', 'tour_field', 'per_person_price', 'thumbnail_img']