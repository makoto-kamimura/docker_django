from django.db import models
from datetime import datetime


class Product(models.Model):

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = "商品"

    name = models.CharField(verbose_name = '製品名', max_length=150, null = False, blank=False)
    price = models.IntegerField(verbose_name = '価格' ,null= True, blank=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):

    class Meta:
        verbose_name = '注文データ'
        verbose_name_plural = '注文データ'

    created_date = models.DateField("注文日",default=datetime.now)
    product = models.ForeignKey(Product, on_delete = models.PROTECT,verbose_name ="製品名")

    def __str__(self):
        return f'注文: {self.created_date.strftime("%Y-%m-%d")}'
