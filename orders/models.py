from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_noop


class Order(models.Model):
    class PaymentMethod(models.IntegerChoices):
        CASH = 1, gettext_noop("CASH")
        CARD = 2, gettext_noop("CARD")

    user = models.ForeignKey(
        User,
        verbose_name=_("User order"),
        on_delete=models.CASCADE,
        related_name="orders",
    )
    ##Verificar
    price = models.FloatField("total price", null=False, blanck=False)
    ##
    send = models.BooleanField(verbose_name=_("send/"), default=False)
    payment_method = models.IntegerField(
        verbose_name=_("Payment method"), choise=PaymentMethod
    )
    created_ad = models.DateField(auto_now=False, auto_now_add=True)


class Pizza(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name=_("Pizza order"),
        on_delete=models.CASCADE,
        related_name="pizza",
    )
    name = models.CharField(verbose_name=_("Name of pizza"), max_length=155)
    description = models.CharField(
        verbose_name=_("Description of pizza"), max_length=155
    )
    amount = models.IntegerField(verbose_name=_("Amount of pizzas"), default=0)
    price = models.FloatField(verbose_name=_("Price of pizza"))
    image = models.ImageField(verbose_name=_("Image of pizza"))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    # def get_display_price(self):
    #     return "{0:.2f}".format(self.price / 100)


class Send(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name=_("Send order"),
        on_delete=models.CASCADE,
        related_name="send",
    )
    address = models.CharField(verbose_name=_("Address of user"), max_length=255)
    number = models.IntegerField(max_length=10, verbose_name=_("Address number"))
    description_extras = models.CharField(
        verbose_name=_("Apartment number, between streets...")
    )
    price = models.FloatField(verbose_name=_("Price of send"), default=200)
