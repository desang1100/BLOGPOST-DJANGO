# this is where my views/rendered html files go
from django.http import HttpResponse


def aboutPage(request):
    return HttpResponse("This is about Page")