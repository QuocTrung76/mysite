from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic


def index(request):
    return render(request,'polls/index.html')
