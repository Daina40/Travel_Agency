from django.contrib import admin
from .models import DestinationModel, GuideModel, TourPackageModel


admin.site.register(DestinationModel)
admin.site.register(GuideModel)
admin.site.register(TourPackageModel)