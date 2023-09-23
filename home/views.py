from django.shortcuts import render, HttpResponse
from datetime import date
from home.models import Contact, Book


# Create your views here.

def index(request):
    
    books = Book.objects.all();
    print(books)
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
