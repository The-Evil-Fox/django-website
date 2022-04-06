from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# def index(request):
#     return HttpResponse("<h1>Hello</h1")


def index(request):
    return render(request, "DocBlog/index.html", context={"date": datetime.today()})
