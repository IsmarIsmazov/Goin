from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Banner
from .serializers import BannerSerializer


# Create your views here.
@api_view(['GET'])
def banner_list(request):
    if request.method == 'GET':
        banner = Banner.objects.all()
        serializer = BannerSerializer(banner, many=True)
        return Response(serializer.data)
    else:
        return Response({'errors': 'only get method'})
