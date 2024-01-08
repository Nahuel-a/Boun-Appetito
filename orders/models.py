from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(
        User, verbose_name=_("order num"), on_delete=models.CASCADE
    )
    ##Verificar 
    price = models.FloatField("total price", null=False, blanck=False)
    ##
    send = models.BooleanField(verbose_name=_("send/"), default=False)
    created_ad = models.DateField(auto_now=False, auto_now_add=True)


class Pizza(models.Model):
    order = models.ForeignKey(
        Order, verbose_name=_("Order num"), on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name=_("Name of pizza"), max_length=155)
    description = models.CharField(
        verbose_name=_("Description of pizza"), max_length=155
    )
    amount = models.IntegerField(verbose_name=_("Amount of pizzas"), default=0)
    price = models.FloatField(verbose_name=_("Price of pizza"))
    image = models.ImageField(verbose_name=_("Image of pizza"))
    is_active = models.BooleanField(default=True)
