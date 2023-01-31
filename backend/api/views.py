# from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from  django.forms.models import model_to_dict #this wil directly prints models to dict not need write 25 to 28 lines
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from products.serializers import ProductSerializer
# Create your views here.

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    #DRF API VIEW
    data = request.data
    serializer = ProductSerializer(data= request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.save()
        print(data)
        return Response(serializer.data)
    return Response({'Error':'Invalid data'},status = 400)