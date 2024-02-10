from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from apps.tour_package.serializers.tour_serializers import DestinationSerializer, GuideSerializer, TourPackageSerializer


class DestinationCreate(APIView):
    def post(self, request):
        # name = request.data.get('destination_name')
        # place_location = request.data.get('location')
        # description = request.data.get('description')
        serializer = DestinationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status.HTTP_201_CREATED)


class GuideCreate(APIView):
    def post(self, request):
        serializer = GuideSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status.HTTP_201_CREATED)

class TourPackageCreate(APIView):
    def post(self, request):
        serializer = TourPackageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status.HTTP_201_CREATED)
