from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, CreateView
from .models import Product
from .forms import ProductForm
# Create your views here.

def index(request):
	return render(request, template_name='app/index.html')

class Start(TemplateView):
	template_name = 'base.html'

class ProductListView(ListView):
	model = Product
	template_engine = 'app/products.html'
	context_object_name = 'products'

class ProductCreateView(CreateView):
	form_class = ProductForm
	template_name = 'app/create.html'
	success_url = reverse_lazy('app:products')

