from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from products.models import Product
from django.views import generic
from .forms import ProductForm

# Create your views here.
class ProductListView(TemplateView):
    template_name="product/products.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productList"] = Product.objects.all().order_by("name")
        return context
    
class ProductFormView(generic.FormView):
    model= Product
    template_name = "product/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('list_product')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return super().form_valid(form)
        return self.form_invalid(form)
