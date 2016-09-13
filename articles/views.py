
from django.shortcuts import render,render_to_response
from articles.models import Article
from django.core.mail import send_mail

# Create your views here.



def latest_article(request):
    article_list = Article.objects.order_by('-id')
    return render(request, 'articles.html', {'article_list': article_list})


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("Enter a search term.")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters.")
        else:
            articles = Article.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                                      {'books': articles, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})

def contact(request):
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
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html',
                              {'errors': errors})