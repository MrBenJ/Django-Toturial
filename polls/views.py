from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello world! You're at the polls index")

def otherSite(request):
	return HttpResponse("You've reached a hidden page! Congrats on figuring out how this works!")
