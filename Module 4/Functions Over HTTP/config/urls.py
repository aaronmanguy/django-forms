from django.contrib import admin
from django.urls import path
from app.views import order, hello, how_old

urlpatterns = [
    path("hello/", hello, name="hello"),
    path("how-old/", how_old, name="how-old"),
    path("order-total/", order, name="order"),
    path('admin/', admin.site.urls),
]
