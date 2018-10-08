from django.shortcuts import render, HttpResponse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'dayfinder/index.html'
	
def index(request):
	return HttpResponse("Welcome")