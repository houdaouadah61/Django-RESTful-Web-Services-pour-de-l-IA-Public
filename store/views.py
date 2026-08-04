from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def home(request):
    products = Product.objects.filter(is_active=True)

    query = request.GET.get("q", "").strip()
    category_id = request.GET.get("category")
    max_price = request.GET.get("max_price")

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    if category_id:
        products = products.filter(category_id=category_id)

    if max_price:
        products = products.filter(price__lte=max_price)

    categories = Category.objects.all()

    context = {
        "products": products,
        "categories": categories,
        "search_query": query,
        "selected_category": category_id,
        "max_price": max_price,
    }

    return render(request, "store/home.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)

    context = {
        "product": product,
    }

    return render(request, "store/product_detail.html", context)