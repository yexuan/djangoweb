
from django.shortcuts import render,render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect,HttpResponse
from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact(request):
    # c = {}
    # c.update(csrf(request))
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                '165627230@qq.com',
                ['165627230@qq.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html',
                              {'errors': errors})

def contact_thanks(request):
    return HttpResponse("Thanks for your contacting")