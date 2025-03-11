from django import forms
from .models import BookInstance
from catalog.models import Book

class BookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['due_back', 'status']
        labels = {
            'due_back': 'Return Date',
            'status': 'Availability Status',
        }
        widgets = {
            'due_back': forms.DateInput(attrs={'type': 'date'}),
        }
        
        


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'isbn', 'genre']

