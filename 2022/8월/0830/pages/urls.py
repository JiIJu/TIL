
from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('index/',views.index , name= 'index'),

    ] # 빈 리스트 생성
# 매칭할 페이지가 없다
