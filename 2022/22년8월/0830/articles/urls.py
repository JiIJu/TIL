from django.contrib import admin
from django.urls import path
from . import views # 현재경로를 의미하는 ,

urlpatterns = [
    
    # 화면추가 path('경로',해당경로를 처리해줄 views.py의 함수이름)
    path('index/',views.index, name='index'),
    path('greeting/',views.greeting,name='greeting'),
    path('dinner/',views.dinner , name = 'dinner'),
    path('throw/',views.throw, name = 'throw'),
    path('catch/',views.catch , name = 'catch'),
    path('hello/<name>/',views.hello , name = 'hello'),
]
