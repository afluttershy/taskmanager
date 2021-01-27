from django.db import models
from datetime import date

# Create your models here.


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    date = models.DateTimeField('Дата', default=date.today())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
