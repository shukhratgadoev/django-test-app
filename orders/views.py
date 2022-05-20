from django.shortcuts import render

# Create your views here.

def orders_page(request):
    return render(request, 'index.html')