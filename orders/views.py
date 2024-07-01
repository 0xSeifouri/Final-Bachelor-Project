from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse

from .models import Order, OrderItem
from .forms import OrderForm
from cart.cart import Cart

@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart)==0:
        return redirect('product_list')

    if request.method == 'POST':
        order_form = OrderForm(request.POST, )

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order = order_obj,
                    product = product,
                    quantity = item['quantity'],
                    price = product.price,
                )
            cart.clear()
            order_form = OrderForm()

    return render(request, 'orders/order_detail.html', context={
        'form': order_form,
    })


