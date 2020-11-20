from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.urls import reverse
from .models import UserFile, UserProfile


# home page
def index(request):
    pdf = UserFile.objects.all()
    return render(request, 'index.html', {'pdf': pdf})


# log in
def log_in(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        usercheck = authenticate(request, username=name, password=password)

        if usercheck:
            login(request, usercheck)
            return HttpResponseRedirect(reverse(index))
        else:
            error = 'Wrong credentials'
            return render(request, 'log_in.html', {'error': error})
    else:
        return render(request, 'log_in.html')


# logout
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))


# signout
def sign_up(request):
    if request.method == 'POST':
        print("hi")
        name = request.POST.get('name')
        password = request.POST.get('password')
        usercheck = UserProfile.objects.filter(name=name).exists()

        if not usercheck:

            new_user = User.objects.create_user(
                username=name,
                password=password,
            )
            user1 = UserProfile.objects.create(
                user=new_user,
                name=name,
                password=password,
            )
            return render(request, 'log_in.html')
        else:
            error = 'User already exists!'
            return render(request, 'sign_up.html', {'error': error})
    else:
        return render(request, 'sign_up.html')


# to facilitate download from model
def download(request, id):
    obj = UserFile.objects.get(id=id)
    filename = obj.pdf.path
    response = FileResponse(open(filename, 'rb'))
    return response
