import datetime
import json
from django.utils import timezone
from django.utils.html import strip_tags
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import requests
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'name': 'Ayshia La Fleur Felizia',
        'class': 'KKI',
        'product_list': product_list,
        'last_login': timezone.localtime(request.user.last_login).strftime('%Y-%m-%d %H:%M:%S') if request.user.last_login else 'Never'
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)
    
def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return JsonResponse({
                "success": True,
                "message": "Account created successfully!",
                "redirect_url": reverse("main:login")
            })

        # Convert form.errors to a simple dict of field: [error messages]
        errors = {field: [str(e) for e in errs] for field, errs in form.errors.items()}
        return JsonResponse({
            "success": False,
            "errors": errors
        })
    
    form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
        
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        response = JsonResponse({'success': True, 'message': 'You have been logged out.'})
        response.delete_cookie('last_login')
        return response

    return JsonResponse({'success': False, 'message': 'Invalid request'})

def edit_product(request, id):
    product = Product.objects.get(pk=id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if form.is_valid():
                form.save()
                return JsonResponse({
                    'success': True,
                    'message': 'Product updated successfully!'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                }, status=400)
        else:
            if form.is_valid():
                form.save()
                return redirect('main:show_main')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'edit_product.html', {'form': form})

@require_POST
def delete_product(request, id):
    try:
        product = Product.objects.get(pk=id, user=request.user)
        product_name = product.name
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            product.delete()
            return JsonResponse({
                'success': True,
                'message': f'"{product_name}" has been deleted successfully!'
            })
        else:
            product.delete()
            messages.success(request, f'Product deleted!')
            return redirect('main:show_main')
            
    except Product.DoesNotExist:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Product not found.'
            }, status=404)
        else:
            return redirect('main:show_main')

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description, 
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        price = strip_tags(data.get("price", ""))
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        new_product = Product(
            name=name, 
            description=description,
            price=price,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    