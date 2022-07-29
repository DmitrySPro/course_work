from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    CATEGORY_CHOICES = [
    ('H', 'Домашние задачи'),
    ('W', 'Рабочие задачи'),
    ('SL', 'Список покупок'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Задача")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    complete = models.BooleanField(default=False, verbose_name="Выполнено")
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='W',verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'