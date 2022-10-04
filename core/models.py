
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    descricao = models.CharField(max_length=40)
    titulo = models.CharField(max_length=80)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.descricao} - {self.titulo} - {self.status}'

class Formação(models.Model):
    nome_instituicao = models.CharField(max_length=100)
    formacao = models.CharField(max_length=100)
    trabalho = models.CharField(max_length=100)
    datinic_for = models.DateField(blank=True, null=True)
    dattermi_for = models.DateField(blank=True, null=True)
    descricao_formacao = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome_instituicao}'


