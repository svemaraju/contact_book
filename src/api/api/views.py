from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, World. \n This is the home url for Demo Contact Book application built by Srikanth Vemaraju.")
