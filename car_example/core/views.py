from django.http import HttpResponse
from django.shortcuts import render
import json

def index(request):
    context = {}
    context["title"] = "Машины"
    with open("../cars.json", "r") as file:
        data = json.load(file)
    context["data"] = data

    return render(request, "core/core.html", context=context)