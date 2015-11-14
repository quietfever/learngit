from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^author/$', views.author, name='author'), #author db
    url(r'^book/$', views.book, name='book'),        #book db
    url(r'^author/search/$', views.authorsearch, name='authorsearch'), #author work
    url(r'^book/(?P<bisbn>[0-9]+)/$', views.bookisbn, name='bookisbn'), #book imformation
    url(r'^delete/(?P<isbn>[0-9]+)/$', views.delete,name="delete"),
    
]
