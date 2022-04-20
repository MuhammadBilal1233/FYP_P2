
# Create your views here.
from ast import Str
from asyncio import constants
from distutils.command.config import config
from msilib.schema import Error
from tokenize import String
from unicodedata import name
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

import pyrebase

from django.http import HttpResponse

from .models import Destination1

config={
    'apiKey': 'AIzaSyDEcARcl_W_J_0izDC5XGyRFo1xHIB97Jg',
    'authDomain': 'esp32demo-a6cd3.firebaseapp.com',
    'databaseURL': 'https://esp32demo-a6cd3-default-rtdb.asia-southeast1.firebasedatabase.app',
    'projectId': 'esp32demo-a6cd3',
    'storageBucket': 'esp32demo-a6cd3.appspot.com',
    'messagingSenderId': '724212216976',
    'appId': '1:724212216976:web:ad1e28c37eea0ced8c9415'
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.
 

 
def index1(request):
    username = database.child('test').child('Username').get().val()
    Password = database.child('test').child('Password').get().val()
    ref = request.POST["ref"]
    pas = request.POST["pass"]
    if (ref == username and Password==pas):
        Name = database.child('test').child('Name').get().val()      
        return render(request,'index1.html',{'Name':Name,'username':username,'password':Password})
    else:
        Error = "You have entered wrong username/password"
        return render(request,'login.html',{'Error':Error})
    
def index(request):
    return render(request,'index.html')

def About(request): 
    
    return render(request,'about.html')

def description(request):
    return render(request,'description.html')
def login(request):
    send_mail(
                'Welcome Email',
                'You have been successfully login.',
                'okbye260@gmail.com',
                ['okbye260@gmail.com'],
                fail_silently=False,
    )
    return render(request,'login.html')


def result(request):
    Name = database.child('test').child('name').get().val()
    Voltage = database.child('test').child('Voltage').get().val()
    Current = database.child('test').child('Current').get().val()
    Power = database.child('test').child('Power').get().val()
    Power_Factor = database.child('test').child('Power_Factor').get().val()
    Units = database.child('test').child('Units').get().val()
    Pre_Units = database.child('test').child('Previous_Month').get().val()
    return render(request,'result.html',{'Name':Name,'Voltage':Voltage, 'Current':Current, 'Power':Power,'Power_Factor':Power_Factor,'Units':Units,'Pre_Units':Pre_Units})
    