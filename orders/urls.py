from rest_framework import routers
from .views import OrderViewSet, PizzaViewSet, SendViewSet

router = routers.DefaultRouter()
router.register("orders", OrderViewSet, "orders")
router.register("pizzas", PizzaViewSet, "pizzas")
router.register("sends", SendViewSet, "sends")

urlpatterns = router.urls
