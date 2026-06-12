from django.shortcuts import render,redirect
from app_bookstore.book import Book

books = {
    '1234567890': Book(None,"Book 1", "Author 1", 10, "1234567890"),
    '2345678901': Book(None,"Book 2", "Author 2", 20, "2345678901"),
    '3456789012': Book(None,"Book 3", "Author 3", 30, "3456789012")
}

def home(request):
    return render(request, 'home.html', {'books': books.values()})

def book(request, isbn):
    return render(request, 'book.html', {'book': books[isbn]})

def add_book(request,isbn=None):
    if request.method == 'POST':
        print("ISBN-ME")
        print(request.POST['isbn'])
        title = request.POST['title'].strip()
        author = request.POST['author'].strip()
        price = request.POST['price'].strip()
        isbn = request.POST['isbn'].strip()
        books[isbn] = Book(None,title, author, price, isbn)
        return redirect("/")
    if isbn is not None:
        book = books[isbn]
        return render(request, 'add-book.html', {'book': book})
    return render(request, 'add-book.html')

def delete(request,isbn):
    if isbn in books:
        del books[isbn]
    return redirect('/')