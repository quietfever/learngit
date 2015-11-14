from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import Book
from .models import Author
# I make a change now 
# Create your views here.

def index(request):    
    return render(request, 'index.html')
def delete(request,isbn):
    bookd = Book.objects.get(Isbn = isbn)
    bookd.delete()
    book_list = Book.objects.order_by('Isbn')[:]
    return render(request, 'book.html', locals())
def book(request):
    book_list = Book.objects.order_by('Isbn')[:]
    return render(request, 'book.html', locals())
def author(request):
    author_list = Author.objects.order_by('AuthorID')[:]
    return render(request, 'author.html', locals()) 
def authorsearch(request):
    if'q' in request.GET:
        query = request.GET['q']
        books = Book.objects.filter(AuthorID__Name  = query)
        return render(request, 'authorsearch.html', locals())
    else:
        query = []
        books=[]
        return render(request, 'authorsearch.html', locals())
def bookisbn(request,bisbn):
        book = Book.objects.get(Isbn = bisbn)
        author = book.AuthorID
        return render(request, 'bookisbn.html',locals())
