# views.py
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Autore, Editore, Libro
from .forms import LibroForm
from rest_framework import generics
from .serializers import LibroSerializer
from rest_framework.pagination import PageNumberPagination

class BookListView(ListView):
    model = Libro
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    ordering = ['anno_edizione']

class BookDetailView(DetailView):
    model = Libro
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        nuovo_autore = form.cleaned_data.get('nuovo_autore')
        nuovo_editore = form.cleaned_data.get('nuovo_editore')

        if nuovo_autore:
            nome_cognome = nuovo_autore.split()
            nome = nome_cognome[0]
            cognome = " ".join(nome_cognome[1:]) if len(nome_cognome) > 1 else ""
            autore, created = Autore.objects.get_or_create(nome=nome, cognome=cognome)
            form.instance.autore = autore
        
        if nuovo_editore:
            editore, created = Editore.objects.get_or_create(ragione_sociale=nuovo_editore)
            form.instance.editore = editore

        return super().form_valid(form)


class BookPagination(PageNumberPagination):
    page_size = 10

class BookListAPI(generics.ListAPIView):
    queryset = Libro.objects.all().order_by('anno_edizione')
    serializer_class = LibroSerializer
    pagination_class = BookPagination

class BookCreateAPI(generics.CreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer