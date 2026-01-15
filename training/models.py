from django.db import models

# Create your models here.
class exe(models.Model):
    title = models.CharField('Название', max_length=50)
    inventory = models.CharField('Инвентарь', max_length=50, default='')
    muscles = models.CharField('Мышцы', max_length=50, default='')
    description = models.TextField('Техника выполнения', max_length=250, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Упражнения'
        verbose_name_plural = 'Упражнения'