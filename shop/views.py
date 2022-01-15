from django.core import paginator
from django.shortcuts import render,get_object_or_404
from shop.models import Product,Category
from django.core.paginator import Paginator

from cart.forms import CartAddProductform

def contact_page(request):
    return render(request,'shop/contactpage.html')

def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True) 

    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'index.html',{'products':products,'categories':categories,'category':category,'page_obj':page_obj}) 

def product_detail(request,id , slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductform()
    return render(request,'shop/detail.html',
    {'product':product,'cart_product_form':cart_product_form})

