from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import item
from .serializers import itemSerializer

@api_view(['GET'])
def item_list(request):
    items = item.object.all()
    serializer = itemSerializer(item, many=true)
    return JsonResponse(serializer.data, self=false)
