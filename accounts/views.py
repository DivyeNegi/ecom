from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from .models import Profile, Order
# Create your views here.




def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Email is not registered! Please sign up.')
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Email is not verified! Please verify the email.')
            return HttpResponseRedirect(request.path_info)

        
        user_obj = authenticate(username = email, password = password)

        if user_obj:
            login(request, user_obj)
            return redirect('/')
        
        messages.warning(request, 'Invalid Email or Password!')
        return HttpResponseRedirect(request.path_info)
        

    if request.user.is_authenticated:
        messages.success(request, 'A user is already logged in!')
        return redirect('/')
    return render(request, 'accounts/login.html')

def create_page(request):
    if request.method == 'POST':
        if 'first_name' not in request.POST:
            if request.POST.get('password')!=request.POST.get('password2'):
                messages.warning(request, 'Passwords do not match!')
                return HttpResponseRedirect(request.path_info)
            request.session['email'] = request.POST.get('email')
            request.session['password'] = request.POST.get('password')
            request.session['password2'] = request.POST.get('password2')
            return render(request, 'accounts/create2.html')
        else:
            email = request.session.get('email')
            password = request.session.get('password')
            password2 = request.session.get('password2')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            user_obj = User.objects.filter(username = email)

            if user_obj.exists():
                messages.warning(request, 'Email is already taken!')
                return HttpResponseRedirect(request.path_info)
            if password!=password2:
                messages.warning(request, 'Passwords do not match!')
                return HttpResponseRedirect(request.path_info)
            
            user_obj = User.objects.create(first_name = first_name, last_name = last_name, email = email, username = email)
            user_obj.set_password(password)
            user_obj.save()

            messages.success(request, 'An email has been sent. Proceed with the steps to verify your email.')
            return redirect(login_page)
    else:
        return render(request, 'accounts/create.html')
    
def get_names(request):
    return render(request, 'accounts/create2.html')

def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token = email_token)
        
        if user.is_email_verified:
            return HttpResponse('User already verified!')
        
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email Token!')
    
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'The user was successfully logged out!')
        return redirect(login_page)
    else:
        messages.warning(request, 'No User was logged in!')
        return redirect(login_page)
    
def cart(request):
    user = request.user
    cart = Order.objects.filter(user = user, is_paid = False)
    print(cart,'hey')
    context = {}
    if cart:
        context = { "cart": cart[0] }

    return render(request, 'accounts/cart.html', context)
    
def orders(request):
    user = request.user
    orders = Order.objects.filter(user = user, is_paid = True)
    print(orders)

    context = { "orders": orders }

    return render(request, 'accounts/orders.html', context)

def clearcart(request):
    cart = Order.objects.filter(user = request.user, is_paid = False)
    cart.delete()
    return redirect('/')
