from django.shortcuts import render, redirect
from django.views import View
from .models import Product

# Create your views here.

class homeView(View):
    def get(self, request):
        return render(request, 'product/home.html')


class addProduct(View):
    def get(self, request):
        return render(request, template_name='product/add_product.html')


    def post(self, request):
        if request.method == "POST":
            name = request.POST['name']
            desc = request.POST['desc']
            price = request.POST['price']
            stocks = request.POST['stocks']
            category = request.POST['category']

            product = Product(name=name, description=desc, price=price, stock_quantity=stocks, category=category)
            product.save()

            return redirect('product:product_list')

        return render(request, template_name='product/add_product.html')


class viewProduct(View):
    def get(self, request):
        data = Product.objects.all()
        return render(request, template_name='product/view_products.html', context={'data':data})


class updateView(View):
    def get(self, request, id):
        product = Product.objects.get(pk=id)
        return render(request, template_name='product/update.html', context={'product':product})

    def post (self, request, id):
        product = Product.objects.get(pk=id)
        if request.method == 'POST':
            product_id = request.POST['product_id']
            name = request.POST['name']
            desc = request.POST['desc']
            price = request.POST['price']
            stocks = request.POST['stocks']
            category = request.POST['category']

            product = Product(product_id=product_id, name=name, description=desc, price=price, stock_quantity=stocks,category=category)
            product.save()

            return redirect('product:product_list')

        return render(request, template_name='product/update.html', context={'product':product})


class deleteView(View):
    def get(self, request, id):
        data = Product.objects.get(pk=id)
        data.delete()
        return redirect('product:product_list')
