from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("This is first project")
def demo(request):
    return HttpResponse("please follow my website")
