from django.urls import path
from website.views import *

urlpatterns = [
    #path('url address' , view)
    path('',index_view),
    path('http-test',http_test),
    path('jason_test',jason_test),
    path('about-view',about_view),
    path('cantact-view',contact_view)

]
     
