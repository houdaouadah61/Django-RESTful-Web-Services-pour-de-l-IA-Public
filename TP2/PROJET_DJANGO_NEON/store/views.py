from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def home(request):
    products = Product.objects.filter(is_active=True)

    return render(
        request,
        "store/home.html",
        {"products": products},
    )


def catalog(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()

    recherche = request.GET.get("recherche", "")
    categorie = request.GET.get("categorie", "")
    prix_min = request.GET.get("prix_min", "")
    prix_max = request.GET.get("prix_max", "")

    if recherche:
        products = products.filter(name__icontains=recherche)

    if categorie:
        products = products.filter(category_id=categorie)

    if prix_min:
        products = products.filter(price__gte=prix_min)

    if prix_max:
        products = products.filter(price__lte=prix_max)

    context = {
        "products": products,
        "categories": categories,
        "recherche": recherche,
        "categorie_selectionnee": categorie,
        "prix_min": prix_min,
        "prix_max": prix_max,
    }

    return render(request, "store/catalog.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
        is_active=True,
    )

    return render(
        request,
        "store/product_detail.html",
        {"product": product},
    )