from django.views.generic import *
from django.shortcuts import render
from django.db.models import Q
from book_store.models import *
from django.http import HttpResponse
import time

def index(request):
    books = {'book_list': Book.objects.all()}
    return render(request, './index.html', context=books)

def contacts(request):
    html = """
        <h2>Biz bilan aloqa</h2>
        <strong>Tel: 93-577-27-04</strong><br>
        <strong>Email: ahmadjoniyimron2003@gmail.com</strong>
    """
    return HttpResponse(html)

def subpage(request):
    return render(request, 'subpage.html')


##### ##### Publisher View ##### #####


class PublisherListView(ListView):
    model = Publisher
    template_name = 'publishers view.html'

    def get_context_data(self):
        q = Publisher.objects.all()
        time.sleep(10)
        url_dict = self.request.GET
        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(name__icontains=text))

        context = {'teachers': q}
        return context


class PublisherCreateView(CreateView):
    model = Publisher
    fields = ['name', 'address', 'city', 'website']
    template_name = 'publishers create.html'
    success_url = '../view/'


class PublisherUpdateView(UpdateView):
    model = Publisher
    fields = ['name', 'address', 'city', 'website']
    template_name = 'publishers update.html'
    success_url = '../view/'

    def get_object(self):
        return Publisher.objects.get(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.object.id
        return context


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'publishers delete.html'
    success_url = '../view/'


##### ##### Student ##### #####


class AuthorListView(ListView):
    model = Author
    template_name = 'authors view.html'

    def get_context_data(self):
        q = Author.objects.all()
        time.sleep(10)
        url_dict = self.request.GET
        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(last_name__icontains = text) | Q(first_name__icontains = text))

        context = {'students': q}
        return context


class AuthorCreateView(CreateView):
    model = Author
    fields = ['salutation', 'name', 'image']
    template_name = 'authors create.html'
    success_url = '../view/'


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['salutation', 'name', 'image']
    template_name = 'authors update.html'
    success_url = '../view/'

    def get_object(self):
        return Author.objects.get(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.object.id
        return context


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors delete.html'
    success_url = '../view/'


##### ##### Book ##### #####


class BookListView(ListView):
    model = Book
    template_name = 'books view.html'

    def get_context_data(self):
        q = Book.objects.all()
        time.sleep(10)
        url_dict = self.request.GET
        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(name__icontains=text))

        context = {'subjects': q}
        return context


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'authors','description', 'price', 'publisher','image']
    template_name = 'books create.html'
    success_url = '../view/'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'authors','description', 'price','publisher','image']
    template_name = 'books update.html'
    success_url = '../view/'

    def get_object(self):
        return Book.objects.get(pk=self.kwargs.get('pk'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.object.id
        return context


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books delete.html'
    success_url = '../view/'
