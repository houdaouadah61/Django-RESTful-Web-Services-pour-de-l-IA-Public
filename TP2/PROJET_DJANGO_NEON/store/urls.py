from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("catalogue/", views.catalog, name="catalog"),
    path(
        "produit/<int:product_id>/",
        views.product_detail,
        name="product_detail",
    ),
]