from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse

def index_view(request):
    return render (request,'page_o/index.html')

def contact_view(request):
    return render (request,'page_o/contact.html')

def about_view(request):
    return render (request,'page_o/about.html')