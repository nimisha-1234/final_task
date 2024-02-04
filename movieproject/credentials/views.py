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


def user_edit(request):
    user = request.user
    print(user.email)
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email

        if not (first_name and last_name and email):
            messages.error(request, 'Invalid Data')
        
        if password1 and password2:
            if password1 == password2:
                
                user.set_password(password1)
                user.save()
                messages.success(request, 'User details updated successfully')
                messages.success(request, 'Please login')
                request.session.flush()
                return redirect('user:perform_logout')
            else:
                messages.error(request, 'Password does not match')
        messages.success(request,'User details updated successfully')
        user.save()
    return render(request,'user_edit.html',{'user':user})