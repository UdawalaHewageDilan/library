from django.contrib import admin

from books.models import Autore, Editore, Libro

# Register your models here.
admin.site.register(Autore)
admin.site.register(Editore)
admin.site.register(Libro)