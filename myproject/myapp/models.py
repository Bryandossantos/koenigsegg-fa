from django.db import models
class MinhaModelo(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='images/')
# Create your models here.
