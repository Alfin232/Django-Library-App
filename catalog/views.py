from django.shortcuts import render, redirect
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.views import generic
from .forms import BookForm

def home(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }
    return render(request, 'home.html', context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_details.html'

@login_required
def my_view(request):
    return render(request, 'my_template.html')





from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BookInstance
from .forms import BookInstanceForm

@login_required
def renew_book(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == "POST":
        form = BookInstanceForm(request.POST, instance=book_instance)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after renewal
    else:
        form = BookInstanceForm(instance=book_instance)

    return render(request, 'catalog/renew_book.html', {'form': form, 'book_instance': book_instance})




def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after successful submission
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
