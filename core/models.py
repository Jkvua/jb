
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nome} - {self.endereco} - {self.email}'

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
        return f'{self.formacao} - {self.trabalho}'

class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome_cidade} - {self.estado}'

class Profissional(models.Model):
    cnpj = models.CharField(max_length=32, null=True, blank=True)
    estado_civil = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    twitter = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.cnpj} - {self.data_nascimento} - {self.estado_civil}'

class Inscrição(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.tempo}'


