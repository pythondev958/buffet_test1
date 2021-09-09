from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def index(request):
    return render(request,"login.html")


def registration(request):
    return render(request, "registration.html")


from datetime import date


def login(request):
    return render(request, "login.html")
from datetime import datetime




def registration2(request):
    name = request.POST['name']
    username = request.POST['username']
    password = request.POST['password']
    now = datetime.now()
    from .models import registration
    obj = registration(name=name, username=username, password=password,timestamp=now)
    obj.save()
    return render(request, "login2.html")

from random import randint as ml_metric
def login_check(request):
    input_username = request.POST['username']
    input_password = request.POST['password']
    from .models import registration

    temp = registration.objects.all()
    usernames = list(temp.values_list('username', flat=True))
    passwords = list(temp.values_list('password', flat=True))

    e = False
    p = False

    if input_username in usernames:
        e = True
    if input_password in passwords:
        p = True

    if e == True and p == True:
        print('success')
        from .models import registration
        temp = registration.objects.all()
        mydata={'dataset':temp}
        return render(request, "index.html",mydata)

    else:
        print('failed')
        return render(request, "login3.html")



