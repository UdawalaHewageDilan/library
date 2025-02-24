import json
from django.core.management.base import BaseCommand
from books.models import Autore, Editore, Libro

class Command(BaseCommand):
    help = 'Importa i dati da db.json nel database'

    def handle(self, *args, **kwargs):
        with open('db.json', encoding='utf-8') as f:
            data = json.load(f)

        # Importa autori
        autori_map = {}
        for autore in data.get('autori', []):
            obj, created = Autore.objects.get_or_create(
                id=autore['id'],
                defaults={'nome': autore['nome'], 'cognome': autore['cognome']}
            )
            autori_map[autore['id']] = obj

        # Importa editori
        editori_map = {}
        for editore in data.get('editori', []):
            obj, created = Editore.objects.get_or_create(
                id=editore['id'],
                defaults={
                    'ragione_sociale': editore['ragione sociale'],
                    'indirizzo': editore.get('indirizzo', ''),
                    'telefono': editore.get('telefono', '')
                }
            )
            editori_map[editore['id']] = obj

        # Importa libri
        for libro in data.get('libri', []):
            autore = autori_map.get(libro['autore'])
            editore = editori_map.get(libro['editore'])
            if autore and editore:
                Libro.objects.get_or_create(
                    titolo=libro['titolo'],
                    autore=autore,
                    editore=editore,
                    anno_edizione=libro.get('anno edizione', None)
                )

        self.stdout.write(self.style.SUCCESS('Importazione completata con successo!'))
