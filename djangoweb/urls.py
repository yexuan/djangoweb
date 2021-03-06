"""djangoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from view import *
from articles import views as articles_views
from contact import views as contact_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',hello),
    url(r'^$',homepage),
    url(r'^time/(\d{1,2})/$',ctime),
    url(r'^ft$',first_template),
    url(r'^anlog$','contact.views.an_log'),
    url(r'^articles/$', articles_views.latest_article),
    url(r'^meta/$', display_meta),
    url(r'^search/$',articles_views.search),
    url(r'^contact/$',contact_views.contact),
    url(r'^contact/thanks/',contact_views.contact_thanks),
    url(r'^home/$', 'contact.views.home', name='home'),
]
