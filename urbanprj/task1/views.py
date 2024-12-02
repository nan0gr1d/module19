# task1.views

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game

users = []

def process_form_data(username, password, repeat_password, age):
    buyers = Buyer.objects.all()
    for buyer in buyers:
        users.append(buyer.name)
    error = ''
    #  if password != repeat_password:
    #,     error = 'Пароли не совпадают'
    #  elif age < 18:
    #,     error = 'Вы должны быть не моложе 18'
    if username in users:
        error = f'Пользователь {username} уже существует!'
    return error

def sign_up_by_django(request):
    info = {}
    error = ''
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            error = process_form_data(username, password, repeat_password, age)
            if not error:
                Buyer.objects.create(name=username,balance=0.0,age=age)
                return HttpResponse(f"<h1>Покупатель {username} добавлен.</h1>")
    else:
        form = UserRegister()
    info = {
        'form': form,
        'error': error,
    }
    return render(request, 'registration_page.html', context=info)

def sign_up_by_html(request):
    error = ''
    form = ''
    info = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        age = int(request.POST.get('age', '0'))
        error = process_form_data(username, password, repeat_password, age)
        if error:
            info = {
                    'form': form,
                    'error': error,
                    'username': username,
                    'password': password,
                    'repeat_password': repeat_password,
                    'age': age
                    }
        else:
            Buyer.objects.create(name=username, balance=0.0, age=age)
            return HttpResponse(f"<h1>Покупатель {username} добавлен.</h1>")

    return render(request, 'registration_page.html', context=info)


def index(request):
    return render(request, 'base.html')

def shop(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'shop.html', context=context)

def cart(request):
    return render(request, 'cart.html')



