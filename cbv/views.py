from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from django.db.models import F
from django.utils import timezone

from .models import Post, Books


def index(request):
    return HttpResponse('statted')


class NewTemp(TemplateView):

    template_name = 'base.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=1)
        context['data'] = 'Context data using TemplateView'
        return context


class IndexView(TemplateView):

    template_name = 'books.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()
        return context

# similar to  TemplateView
# in Listview pagination allowed
class BookListView(ListView):

    model = Books
    template_name = 'books.html'
    context_object_name = 'books'
    paginate_by = 4
    # we can controll the view usting query_set (or get_queryset())
    #queryset = Books.objects.all()[:3]

#using query_set and get_queryset both are exactly same operations
    def get_queryset(slef):
        return Books.objects.all()[:3]


class GenereView(ListView):

    model = Books
    template_name = 'books.html'
    context_object_name = 'books'
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))


# can't use pagination in Detail view
# only allowed data from single model
class BookDetailView(DetailView):

    model = Books
    template_name = 'book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        book = Books.objects.filter(slug=self.kwargs.get('slug'))
        book.update(count=F('count') + 1)

        context['time'] = timezone.now()
        return context




