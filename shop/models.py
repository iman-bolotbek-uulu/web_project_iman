from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование товара')
    price = models.IntegerField(verbose_name='Цена товара')

class Purchase(models.Model):
    name = models.CharField(max_length=30,verbose_name='ФИО клиента')
    age = models.IntegerField(verbose_name='Возраст клинта')
    item = models.ForeignKey(Item,on_delete=models.CASCADE,related_name='purchases')
    date_purchase = models.DateField(verbose_name='Дата покупки')
