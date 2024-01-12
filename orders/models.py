from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_noop


class Pizza(models.Model):
    name = models.CharField(max_length=155, verbose_name=_("Name of pizza"))
    description = models.CharField(
        verbose_name=_("Description of pizza"), max_length=155
    )
    price = models.FloatField(verbose_name=_("Price of pizza"))
    image = models.ImageField(verbose_name=_("Image of pizza"), null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Send(models.Model):
    address = models.CharField(max_length=255, verbose_name=_("Address of user"))
    number = models.IntegerField(verbose_name=_("Address number"))
    description_extras = models.CharField(
        max_length=500, verbose_name=_("Apartment number, between streets...")
    )
    price = models.FloatField(verbose_name=_("Price of send"), default=200)


class Order(models.Model):
    class PaymentMethod(models.IntegerChoices):
        CASH = 1, gettext_noop("CASH")
        CARD = 2, gettext_noop("CARD")

    user = models.ForeignKey(
        User,
        verbose_name=_("User order"),
        on_delete=models.CASCADE,
        related_name="user_order",
    )
    pizza = models.ForeignKey(
        Pizza,
        verbose_name=_("Pizza order"),
        on_delete=models.CASCADE,
        related_name="pizza_order",
    )
    send_order = models.ForeignKey(
        Send,
        verbose_name=_("Send order"),
        on_delete=models.CASCADE,
        related_name="send_order",
        null=True,
        blank=True,
    )
    price = models.FloatField(verbose_name=_("Total price"), default=0)
    send = models.BooleanField(verbose_name=_("send"), default=False)
    payment_method = models.IntegerField(
        verbose_name=_("Payment method"), choices=PaymentMethod.choices
    )
    created_ad = models.DateField(auto_now=False, auto_now_add=True)

    def get_display_price(self):
        return "{0:.2f}".format(self.price)

    def save(self, *args, **kwargs):
        if self.send:
            send_price = self.send_order.price
            pizzas_in_order = self.pizza
            pizzas_price = sum(pizza.price for pizza in pizzas_in_order)

            self.price = pizzas_price + send_price
        else:
            pizzas_in_order = self.pizza
            pizzas_price = sum(pizza.price for pizza in pizzas_in_order)
            self.price = pizzas_price

        super(Order, self).save(*args, **kwargs)
