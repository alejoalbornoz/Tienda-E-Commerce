
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate 
from django.contrib.auth import  login, logout
from django.contrib import messages
from TiendaOnline.forms import RegisterForm
from products.models import Product

from users.models import User





def index(request):

    products = Product.objects.all().order_by("id")


    return render (request,'index.html', {
        "message":"Listado de productos",
        "title":"Productos",
        "products": products,
    })

def login_view (request):

    if request.user.is_authenticated:
        return redirect ("index")



    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Bienvenido {}".format(user.username))
            return redirect("index")
        else: 
            messages.error(request, "Usuario o contraseña no validos")
            

    return render(request, "users/login.html",{

    })

def logout_view (request):
    logout(request)
    messages.success(request, "Sesion cerrada exitosamente")
    return redirect ("login")

def register(request):

    if request.user.is_authenticated:
        return redirect ("index")

    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, "Usuario creado exitosamente")
            return redirect("index")
        
            
    return render (request, "users/register.html", {
        'form': form 
    })
