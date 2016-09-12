#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect,HttpResponse
from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt
from forms import ContactForm
import json

@csrf_exempt
def contactOld(request):
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
            # send_mail(
            #     request.POST['subject'],
            #     request.POST['message'],
            #     '165627230@qq.com',
            #     ['165627230@qq.com'],
            # )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html',
                              {'errors': errors})
@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('email', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            # )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render_to_response('contact_form.html', {'form': form})


def home(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render(request, 'home.html', {
            'List': json.dumps(List),
            'Dict': json.dumps(Dict)
        })

def contact_thanks(request):
    return HttpResponse("Thanks for your contacting")


def an_log(request):
    d = {'1.htldxhzj.duapp.com': 9398,
         'gtxapi.cdn.duapp.com': 79496,
         'www.xxx.com': 2477070,
         'www.baidu.com': 1465,
         'www.bing.com': 777,
         'www.aaa.com': 1113101,
         'www.ccc.net.cn': 922,
         'www.zhanimei.ga': 29847,
         'www.zhanimei.ml': 40155,
         'www.zhasini.ml': 373436}
    categories = d.keys()
    data = d.values()
    return render_to_response('an_log.html', {'user': request.user, 'categories': categories, 'data': data})