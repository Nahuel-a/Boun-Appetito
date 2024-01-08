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
