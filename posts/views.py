
# Create your views here.
from django.http import HttpResponse
from datetime import datetime


def hello(request):
    return HttpResponse("Hello! It's my project")


def now_date(request):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(current_date)


def goodbye(request):
    return HttpResponse("Goodbye user!")
