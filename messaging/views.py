from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, MessageForm
from passlib.context import CryptContext
from .models import User as UserModel
from .forms import Messages
from django.contrib.auth import login, authenticate

# Create your views here.
global_username = ""


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_object = form.save(commit=False)
            hashed_password = hash_password(form.cleaned_data["password"])
            user_object.password = hashed_password
            user_object.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "messaging/register.html", {"form": form})


def hash_password(password):
    crypt_cxt = CryptContext(schemes=["bcrypt"])
    return crypt_cxt.hash(password)


def index(request):
    return render(request, "messaging/index.html", )


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form_username = form.cleaned_data["username"]
            form_password = form.cleaned_data["password"]
            user = UserModel.objects.filter(username=form_username)[0]
            if user:
                crypt_cxt = CryptContext(schemes=["bcrypt"])
                is_valid = crypt_cxt.verify(form_password, user.password)
                if is_valid:
                    global_username = user.username
                    return redirect('dashboard')
    else:
        form = UserLoginForm()
    return render(request, "messaging/login.html", {"form": form})


def dashboard(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        print(global_username)
        if form.is_valid():
            message_object = form.save(commit=False)
            message_object.sender = global_username

            message_object.save()
            return redirect('login')
    else:
        form = MessageForm()

    context = {"form": form}
    return render(request, "messaging/dashboard.html", context)
