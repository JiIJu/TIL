
from django.contrib import admin
from django.urls import path , include
from articles import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # # 화면추가 path('경로',해당경로를 처리해줄 views.py의 함수이름)
    # path('index/',views.index),
    # path('greeting/',views.greeting),
    # path('dinner/',views.dinner),
    # path('throw/',views.throw),
    # path('catch/',views.catch),
    # path('hello/<name>/',views.hello),
    path('admin/',admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
