from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            print('logged in')
            auth.login(request,user)
            print('user log')
            return redirect('/')

        else:
            messages.info(request,'invalid Username')
            return redirect('/')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        userName = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']
        passwordConfirm = request.POST['passwordConfirm']
        if password==passwordConfirm:
            if User.objects.filter(username=userName).exists():
                messages.info(request,'Username Taken')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'You Already have an account..!!!')
            else:
                user = User.objects.create_user(username=userName,email=email,password=password,first_name=firstName,last_name=lastName)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not match')
        return redirect('signup')
    return render(request,'signup.html')