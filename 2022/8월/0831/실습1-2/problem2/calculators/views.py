from django.shortcuts import render

# Create your views here.
def result(request):
    return render(request,'result.html')


def calculation(request):
    return render(request,'calculation.html')