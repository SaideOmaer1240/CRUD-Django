from django.db import models
from django.conf import settings

class Ativo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nome do Ativo')
    valor = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True )
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Ativo'
        verbose_name_plural = 'Ativos'

class Passivo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nome do passivo')
    valor = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True )

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Passivo'
        verbose_name_plural = 'Passivos'
    