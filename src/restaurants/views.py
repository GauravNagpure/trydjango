import random
from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    num = random.randint(0, 25)
    return render(request, "base.html", {"hello": "try django", "num": num, "num_": num * num})
# Create your views here.
