from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse ('http_test')

def jason_test(request):
    return JsonResponse ({'name':'ali'})

def index_view(request):
    return HttpResponse ('<h1> HOME PAGE </h1>')

def contact_view(request):
    return HttpResponse ('<h1> CONTACT PAGE </h1>')

def about_view(request):
    return HttpResponse ('<h1> ABOUT PAGE </h1>')