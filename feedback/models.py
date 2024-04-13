from django.db import models
from django.conf import settings
# Create your models here.
class Feedback(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sugestao = models.CharField(verbose_name='Sua sugestão de melhoria ou adição de recursos', max_length=50, null=True, blank=True)
    descrition = models.TextField(verbose_name='Descrição da sua sugestão para melhoria')
    
    def __str__(self):
        return self.sugestao