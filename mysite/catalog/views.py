from django.shortcuts import render

from .models import Product


def home(request):
    max_price = request.GET.get('max price','')
    products = Product.objects.all()
    if max_price:
        budget = int(max_price)
        products + products.filter(price_lte = budget)
    return render(request, 'products_list.html', {
        'products': products, 
        "show_budjet": True,
        'max_price': max_price,

})
