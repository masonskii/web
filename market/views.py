from django.shortcuts import render

# Create your views here.
from market.models import Product


def sell(request):
    if request.method == 'POST':
        pass
    else:
        products = Product.objects.all()
        logo = []
        return render(
            request,
            'market.html',
            {
                'products': products,
            }
        )
