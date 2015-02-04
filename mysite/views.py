from django.shortcuts import render
from django.http import HttpResponse

# Home level views

def index(request):
	return HttpResponse("Welcome to the home page!")

