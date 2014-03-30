from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render_to_response


def index(request):
	response = {}
	response["title"]="Welcome to QiQi E-shop"
	return render_to_response('index.html',response)
