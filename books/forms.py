from django import forms
from .models import Libro, Autore, Editore

class LibroForm(forms.ModelForm):
    nuovo_autore = forms.CharField(required=False, max_length=100, label="Nuovo Autore")
    nuovo_editore = forms.CharField(required=False, max_length=200, label="Nuovo Editore")

    class Meta:
        model = Libro
        fields = ['titolo', 'autore', 'editore', 'anno_edizione']

    def clean(self):
        cleaned_data = super().clean()
        nuovo_autore = cleaned_data.get("nuovo_autore")
        nuovo_editore = cleaned_data.get("nuovo_editore")
        autore = cleaned_data.get("autore")
        editore = cleaned_data.get("editore")

        if nuovo_autore and autore:
            self.add_error("nuovo_autore", "Seleziona un autore esistente o creane uno nuovo, non entrambi.")
        elif not nuovo_autore and not autore:
            self.add_error("autore", "Devi selezionare un autore o crearne uno nuovo.")

        if nuovo_editore and editore:
            self.add_error("nuovo_editore", "Seleziona un editore esistente o creane uno nuovo, non entrambi.")
        elif not nuovo_editore and not editore:
            self.add_error("editore", "Devi selezionare un editore o crearne uno nuovo.")

        return cleaned_data
