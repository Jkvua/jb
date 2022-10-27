from django.db import models


class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_cidade} - {self.estado}"


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, related_name="+")

    def __str__(self):
        return f"{self.nome} - {self.endereco} - {self.email}"


class Vaga(models.Model):
    descricao = models.CharField(max_length=40)
    titulo = models.CharField(max_length=80)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} - {self.titulo} - {self.status}"


class Inscrição(models.Model):
    descricao = models.CharField(max_length=100)
    vaga = models.ForeignKey(Vaga, on_delete=models.PROTECT, related_name="+")

    def __str__(self):
        return f"{self.descricao} - {self.vaga}"


class Formação(models.Model):
    nome_instituicao = models.CharField(max_length=100)
    formacao = models.CharField(max_length=100)
    trabalho = models.CharField(max_length=100)
    datinic_for = models.DateField(blank=True, null=True)
    dattermi_for = models.DateField(blank=True, null=True)
    descricao_formacao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.formacao} - {self.trabalho}"


class Profissional(models.Model):
    CPF = models.CharField(max_length=32, null=True, blank=True)
    estado_civil = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.CPF} - {self.data_nascimento} - {self.estado_civil}"

class Expreriencias(models.Model):
    descricao_experiencia = models.CharField(max_length=32)
    data_inicio = models.DateField(blank=True, null=True)
    data_termino = models.DateField(blank=True, null=True)
    experiencias1 = models.TextField(max_length=200)
    experiencias2 = models.TextField(max_length=32)
    experiencias3 = models.TextField(max_length=32)

    def __str__(self):
        return f"{self.descricao_experiencia} - {self.experiencias1}"
