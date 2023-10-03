from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
# from django.contrib.auth import login,authenticate,logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
# import requests
import json
from datetime import date


# def get_Books_data(number):

#     api_url = f"https://frappe.io/api/method/frappe-library?page={number}&title=and"
#     response = requests.get(api_url)
#     data = response.json()

#     return data

    # api_url =  f"https://frappe.io/api/method/frappe-library?page=2&title=and"
    # response = requests.get(api_url)
    # data = response.json()
    # text = json.dumps(data, sort_keys=True, indent=4)
    # return text


def home(request):
    
    return render(request, 'home.html')


@login_required(login_url="/login_user")
def book_view(request):
    queryset = FetchBook.objects.all()
    paginator = Paginator(queryset, 20) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, "viewFeatchData.html", {"queryset": page_obj})


def signUp(request):
    if (request.method == 'POST'):
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        userAuth = User.objects.filter(username=username)
        if (userAuth.exists()):
            messages.info(request, 'Username Alraday exists!')
            return redirect('/register')

        queryset = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        queryset.set_password(password)
        queryset.save()
        messages.info(request, 'Account Create Successfully!')
        return redirect('/book_view')
    return render(request, 'signUp.html')


def login_user(request):
    if (request.method == 'POST'):
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        # if username doesn't exists then message to the user.
        user = User.objects.filter(username=username)
        if (not user.exists()):
            messages.error(request, 'Username Does not exists!')
            return redirect('/login_user')
        # cheak  account ahea ka nahi
        userAuth = authenticate(username=username, password=password)
        if (userAuth is None):
            messages.error(request, 'Account does not exists')
            return redirect('/login_user')
        else:
            # acccout assel ther value fit houn user login hoil
            login(request, userAuth)
            return redirect('/')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/login_user')


# def register(request):
#     if (request.method == 'POST'):
#         data = request.POST
#         name = data.get('name')
#         age = data.get('age')
#         email = data.get('email')
#         street_address = data.get('street_address')
#         state = data.get('state')
#         city = data.get('city')
#         postal_code = data.get('postal_code')
#         queryset = Member.objects.create(
#             name=name,
#             age=age,
#             email=email,
#             amount_limit=500
#         )
#         queryset2 = Address.objects.create(
#             street_address=street_address,
#             city=city,
#             state=state,
#             postal_code=postal_code

#         )
#         queryset2.save()
#         queryset.save()

#         messages.info(request, "Register User Succsessfully!")
#         return redirect('/register')

#     return render(request, 'register.html')



def getDetails(request,book_id):
    queryset = FetchBook.objects.filter(book_id = book_id)
    context = {
        'queryset':queryset
    }
    return render(request, 'bookDetails.html', context)
    
    














