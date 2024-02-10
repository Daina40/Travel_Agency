from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from apps.tour_package.serializers.tour_serializers import DestinationSerializer, GuideSerializer, TourPackageSerializer
from apps.tour_package.models import DestinationModel, GuideModel, TourPackageModel


class DestinationCreate(APIView):
    def post(self, request):
        serializer = DestinationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def get(self, request):
        queryset = DestinationModel.objects.all()
        serializer = DestinationSerializer(queryset, many=True)
        return Response(serializer.data)
    

class GuideCreate(APIView):
    def post(self, request):
        serializer = GuideSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status.HTTP_201_CREATED)
    
    def get(self, request):
        queryset = GuideModel.objects.all()
        serializer = GuideSerializer(queryset, many=True)
        return Response(serializer.data)

class TourPackageCreate(APIView):
    def post(self, request):
        serializer = TourPackageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status.HTTP_201_CREATED)
    
    def get(self, request):
        queryset = TourPackageModel.objects.all()
        serializer = TourPackageSerializer(queryset, many=True)
        return Response(serializer.data)
