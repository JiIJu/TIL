from django.shortcuts import render
import random
# Create your views here.
def index(request):
    # request : 사용자의 요청정보가 담겨있다.
    # 사용자에게 보여줄 화면 html 파일 이름
    return render(request,'index.html')

# def greeting(request):
#     return render(request,'greeting.html',{'name':'지이주'})


def greeting(request):
    foods = ['apple','banana','coconut']
    info = {
        'name' : '지이주',
        'age' : 26
    }
    context = {
        
        'foods' : foods,
        'info' : info,
    }
    return render(request,'greeting.html',context)

def dinner(request):
    foods = ['족발','햄버거','치킨','초밥','오리불고기']
    pick = random.choice(foods)

    context = {
        'pick' : pick,
        'foods' : foods,
        'number' : 0
    }
    return render(request,'dinner.html',context)

def throw(request):
    return render(request,'throw.html')

def catch(request):
    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get('message'))


    message = request.GET.get('message')
    context = {'message' : message}

    return render(request,'catch.html',context)

def hello(request,name):
    context = {
        'name' : '지이주',
    }

    return render(request,'hello.html',context)