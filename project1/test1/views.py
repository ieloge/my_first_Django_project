from django.shortcuts import render, HttpResponse,redirect
from .models import Contact_Querry, Product
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    product_info=Product.objects.all()
    print(product_info)
    return render(request, 'test1/home.html',{'product_info':product_info})
    #return HttpResponse('<h1>Home Page</h1>')
    
    

def contact(request):
    return HttpResponse('Contact Page')

@login_required(login_url='loginuser')
def product (request):
    product_info = Product.objects.all()
    paginator = Paginator(product_info, 3)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'test1/product.html', {'page_obj': page_obj})

def contact(request):
    if request.method == 'GET':
     return render(request, 'test1/contact.html')
    else:
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('subject') or "General Inquiry"
        d = request.POST.get('message')
        new_data = Contact_Querry(name=a, email=b, subject=c, message=d)
        new_data.save()
        return render(request, 'test1/contact.html', {'success': True})
    
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'test1/loginuser.html',{'form':AuthenticationForm()})
    else:
        a= request.POST.get('username')
        b= request.POST.get('password')
        user = authenticate(request, username=a, password=b)
        if user is None:
            return render(request, 'test1/loginuser.html',{'form':AuthenticationForm(),'error':'Username or password is incorrect'})
        else:
            login(request, user)
            return redirect('home')
        
        

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'test1/signupuser.html', {
            'form': UserCreationForm()
        })

    form = UserCreationForm(request.POST)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')

    return render(request, 'test1/signupuser.html', {
        'form': form
    })
    

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')