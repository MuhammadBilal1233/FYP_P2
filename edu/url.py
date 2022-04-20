from unicodedata import name
from django.urls import URLPattern,path

from . import views

urlpatterns = [
        path('',views.index,name='index'),
        path('about',views.About,name='about'),
        path('result',views.result,name='result'),
        path('login',views.login,name='login'),
        path('index1',views.index1,name='index1'),
        path('description',views.description,name='description'),
]

