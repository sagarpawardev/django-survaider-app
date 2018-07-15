from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import json

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from survaider_app_module.services.MaleFemaleDistService import MaleFemaleDistService
from survaider_app_module.services.FullDataService import FullDataService
from survaider_app_module.services.RelationshipDistService import RelationshipDistService
from json import JSONEncoder

class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__  

def hello(request):
   text = """<h1>Hello Sagar !</h1>"""
   return HttpResponse(text)

@csrf_exempt
def male_female_dist(request):
	response = MaleFemaleDistService().process()
	return JsonResponse(response)

def full_data(request, page_no):
	size = request.GET.get('size')
	print("*** size ****", size)
	try:
		page_no = int(page_no)
	except:
		page_no = 0

	try:
		size = int(size)
	except:
		size = 30

	response = FullDataService().process(page_no, size)
	response = json.dumps(response)
	#return JsonResponse(response)
	return HttpResponse(response)

def rel_dist(request):
	response = RelationshipDistService().process()
	response = json.dumps(response)
	#return JsonResponse(response)
	return HttpResponse(response)
