from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 

 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def index2(request, val1=0):
    try:
        val1 = int(val1)  
        return HttpResponse(f"value1 = {val1}")
    except ValueError:
        return HttpResponse("Error, expected val1 to be an integer")
    
def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/one_book.html', context)


def links(request):
    return render(request, 'bookmodule/links.html')


def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')


def tables(request):
    return render(request, 'bookmodule/tables.html')

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')


def __getBooksList():
    book1 = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley',price=120, edition = 3)
    book1.save()
    book2 = Book(title = 'Reversing: Secrets of Reverse Engineer', author = 'E.Eilam',price=97, edition = 2)
    book2.save()
    book3 = Book(title = 'The Hundred-Page Machine Learning Book', author = 'Andriy Burkov',price=100, edition = 4)
    book3.save()
    return [book1, book2, book3]

def book(request):
    return render(request, 'bookmodule/bookList.html',{'books':__getBooksList()})


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

 



 

