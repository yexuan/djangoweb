from django.http import HttpResponse

def hello(req):
    return HttpResponse("<h1>lllllll</h1>")

def homepage(req):
    return HttpResponse("<p>This is homepage</p>")