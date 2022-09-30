from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Vagas(models.Models):
    descricao = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descricao
