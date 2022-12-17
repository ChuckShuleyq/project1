from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название города')
    slug = models.CharField(max_length=50, blank=True)
    class Meta:
        verbose_name = "Название населённого пункта"
        verbose_name_plural = "Названия населённых пунктов"
    #переопределение названия добавленного объекта
    def __str__(self):
        return self.name