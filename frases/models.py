from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome

class Fraseologia(models.Model):
    titulo = models.CharField(max_length=200, unique=True, verbose_name="Título da Fraseologia")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    conteudo_template = models.TextField(verbose_name="Conteúdo do Template")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Fraseologia"
        verbose_name_plural = "Fraseologias"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
