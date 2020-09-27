from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    login_url = 'account_login'
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(LoginRequiredMixin, DetailView):
    login_url = 'account_login'
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
