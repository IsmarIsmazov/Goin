from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Recommendation
from .serializers import RecommendationSerializer


# Create your views here.
class RecommendationView(ListAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
