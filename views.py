from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def authview(request):
    return HttpResponse('Django Authentication system')
