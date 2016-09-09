from django.http import HttpResponse, Http404
import datetime
from django import template

def hello(req):
    return HttpResponse("<h1>lllllll</h1>")


def homepage(req):
    return HttpResponse("<p>This is homepage</p>")


def ctime(req, num):
    t = template.Template(open("D:\\_proj\\djangoweb\\templates\\current_time.html").read())
    curtime = datetime.datetime.now()
    c = template.Context({'ctime':curtime})
    try:
        num = int(num)
        num = str(num)
    except Exception as e:
        raise Http404
    content = t.render(c)
    return HttpResponse(content)

def ec(req, num):
    t = template.Template(open("D:\\_proj\\djangoweb\\templates\\ec.html").read())

    return HttpResponse(t)


def first_template(req):
    raw_template = """
    	<p>Dear {{ person_name }},</p>

    	 <p>Thanks for placing an order from {{ company }}. It's scheduled to
    	 ship on {{ ship_date|date:"F j, Y" }}.</p>

    	 {% if ordered_warranty %}
    	 <p>Your warranty information will be included in the packaging.</p>
    	 {% else %}
    	 <p>You didn't order a warranty, so you're on your own when
    	 the products inevitably stop working.</p>
    	 {% endif %}

    	 <p>Sincerely,<br />{{ company }}</p>
    """
    t = template.Template(raw_template)
    c = template.Context({'person_name': 'John Smith', 'company': 'Outdoor Equipment', 'ship_date': datetime.date(2009, 4, 2),
                 'ordered_warranty': False})
    content = t.render(c)
    return HttpResponse(content)

