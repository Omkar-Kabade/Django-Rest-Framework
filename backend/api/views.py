# from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from  django.forms.models import model_to_dict #this wil directly prints models to dict not need write 25 to 28 lines
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from products.serializers import ProductSerializer
# Create your views here.

@api_view(['POST','GET'])
def api_home(request, *args, **kwargs):
    #DRF API VIEW
    instance = Product.objects.all().order_by("?").first( ) # queries randomly
    data = {}
    if instance:
        #data= model_to_dict(instance,fields=['id','title','content','price']) #this wil directly prints models to dict not need write 25 to 28 lines
        data = ProductSerializer(instance).data   #this wil directly prints models to dict not need write 25 to 28 lines
    return Response(data)