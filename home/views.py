from django.shortcuts import render, HttpResponse
from datetime import date
from home.models import Contact, Book

# Create your views here.

def index(request):
    
    books = Book.objects.all()
    return render(request, 'index.html', {'books' : books})

def categoryFilterView(request):

    path = request.path
    print(path)
    categoryString = ""
    if(path == '/fiction'):
        categoryString = 'Fiction'
    elif(path == '/non-fiction'):
        categoryString = 'Non-Fiction'
    elif(path == '/horror'):
        categoryString = 'Horror'
    elif(path == '/children-books'):
        categoryString = 'Children Books'
    elif(path == '/thriller'):
        categoryString = 'Thriller'
    # return HttpResponse(categoryString)
    books = Book.objects.raw('select * from home_book where category = %s', [categoryString])
    return render(request, 'index.html', {'books' : books})


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        dte = date.today()
        contact = Contact(name = name, email=email,phone=phone, desc=desc, date=dte)
        contact.save()
    return render(request, 'contact.html')

def addNewBookForm(request):
    return render(request, 'newBook.html')

def addNewBook(request):
    if(request.method == "POST"):
        bookTitle = request.POST.get("title")
        isbn = request.POST.get("isbn")
        sellingprice = request.POST.get("sellPrice")
        category = request.POST.get("category")
        author = request.POST.get("author")
        newBook = Book(title = bookTitle, ISBN_Number = isbn, selling_Price = sellingprice, category=category, author = author)
        newBook.save()
    return render(request, 'newBook.html')
