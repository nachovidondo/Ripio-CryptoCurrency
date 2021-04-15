from django.db import models



class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200, verbose_name="Moneda", unique=True
        )
    image = models.ImageField(verbose_name="Logo", blank=True, null=True)
    amount = models.FloatField(verbose_name="Cantidad")
    
    class Meta:
        verbose_name="Moneda"
        verbose_name_plural="Monedas"
        
    def __str__(self):
        return self.name