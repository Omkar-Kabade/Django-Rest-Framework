# from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from  django.forms.models import model_to_dict #this wil directly prints models to dict not need write 25 to 28 lines
# Create your views here.

def api_home(request, *args, **kwargs):
    #here request is the instance of HttpRequest Class = request -> HttpRequest which is of django not of python 
    # body = request.body# this gives the byte string of json data ERROR COMING
    # print(request.GET) #print query params of endpoint
    # data = {}
    # try:
    #     data = json.loads(body) #this converts json string to python dict
    # except:
    #     pass
    # print(body)
    # data['content_type'] = request.content_type
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)

    model_data = Product.objects.all().order_by("?").first( ) # queries randomly
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data= model_to_dict(model_data,fields=['id','title','content','price']) #this wil directly prints models to dict not need write 25 to 28 lines
    return JsonResponse(data)