from django.urls import path
from . import views

app_name = 'record'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('home/',views.home,name='home'),
    path('chart/',views.chart,name='chart'),
    path('live/',views.live,name='live'),
    path('totalrecord/',views.totalrecord, name='totalrecord'),
    path('create/',views.create,name='create'),
    path('deepcreate/',views.deepcreate,name='deepcreate'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('stream2/',views.stream2,name='stream2'),
    path('page404/',views.page404,name='page404'),
    path('test/',views.test,name='test'),
]