from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tovar(models.Model):
    STAT = (('П','Продукты'),('О','Одежда'),('Ш','Для школы'),('Д','Для дома'))
    name = models.CharField(max_length=100,
                            verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    image = models.FileField(verbose_name='Картинка',
                             upload_to='img/',
                             blank=True, null=True)
    discount = models.IntegerField(verbose_name='Скидка',
                                 default=0)
    category = models.CharField(choices=STAT, max_length=100,
                                blank=True, null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    tovar = models.ForeignKey(to=Tovar, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество')
    summa = models.DecimalField(verbose_name='Сумма',
                                max_digits=8,
                                decimal_places=2)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def calcSumma(self):
        return self.count*(self.tovar.price - self.tovar.discount/100*self.tovar.price)

class Order(models.Model):
    STAT = (('в сборке','в сборке'),('в пути','в пути'),('доставлен','доставлен'))
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    adres = models.CharField(max_length=100, verbose_name='Адрес')
    tel = models.CharField(max_length=100, verbose_name='Телефон')
    items = models.ManyToManyField(to=Tovar)
    zakaz = models.TextField(verbose_name='Заказ')
    status = models.CharField(choices=STAT, max_length=100)
    total = models.DecimalField(verbose_name='Итог',
                                max_digits=8,
                                decimal_places=2, blank=True, null=True)
