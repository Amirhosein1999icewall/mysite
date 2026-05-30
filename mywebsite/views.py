from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse ('http_test')

def jason_test(request):
    return JsonResponse ({'name':'ali'})