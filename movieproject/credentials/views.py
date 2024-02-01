from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print("LOGIN SUCCESSFULL")
            return redirect('/')
        else:
            print("invalid credentials")
            return redirect('login')
    else:
        return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                print("Username Taken")
                return redirect('/')
            else:
                if User.objects.filter(email=email).exists():
                    print("email taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                    last_name=lastname, email=email)
                    user.save()
                    return redirect('/')

        else:
            print("PASSWORD DID NOT MATCH")
            return redirect('register')
    else:
        return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
