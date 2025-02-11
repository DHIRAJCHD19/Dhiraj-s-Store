from django.shortcuts import render

# Homepage view
def home(request):
    return render(request, 'store/home.html')

# Product list view for men's and women's wear
def product_list(request):
    return render(request, 'store/product_list.html')

# About page view
def about(request):
    return render(request, 'store/about.html')

# Contact page view
def contact(request):
    return render(request, 'store/contact.html')

# Single product page view
def single_product(request):
    return render(request, 'store/single-product.html')