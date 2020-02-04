# i have created this file--- Arpit Rai
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello everyone")
def about(request):
    return HttpResponse("<h1>About everyone</h1>")