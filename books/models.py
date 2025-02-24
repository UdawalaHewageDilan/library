from django.db import models

class Autore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} {self.cognome}"

class Editore(models.Model):
    ragione_sociale = models.CharField(max_length=200)
    indirizzo = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.ragione_sociale

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titolo = models.CharField(max_length=255)
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE)
    editore = models.ForeignKey(Editore, on_delete=models.CASCADE)
    anno_edizione = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titolo