from django.http import HttpResponse,Http404
import datetime

def hello(req):
    return HttpResponse("<h1>lllllll</h1>")

def homepage(req):
    return HttpResponse("<p>This is homepage</p>")

def ctime(req,num):
    curtime = datetime.datetime.now()
    try:
        num = int(num)
        num = str(num)
    except Exception as e:
        raise Http404
    content = "This page is No. %s and tt's %s now" % (num,curtime)
    return HttpResponse(content)