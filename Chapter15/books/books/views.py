from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    login_url = 'account_login'
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = 'account_login'
    permission_required = 'books.special_status'
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'


class SearchResultsView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    # queryset = Book.objects.filter(title__icontains='beginners')

    def get_queryset(self):
        return Book.objects.filter(
            Q(title__icontains='beginners') | Q(title__icontains='api')
        )
