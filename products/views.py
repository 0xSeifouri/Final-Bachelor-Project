from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse
from.models import Product, Comment
from .forms import CommentForm
from cart.forms import AddToCartProductForm

class ProductsListView(generic.ListView):
    queryset = Product.objects.filter(active=True).order_by('-datetime_created')
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductsDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        context['add_to_cart_form']=AddToCartProductForm()
        return context




class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        return super().form_valid(form)

