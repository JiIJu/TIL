from django.shortcuts import render, redirect
# from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Chatting
from .forms import ChattingForm


# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    chatting = Chatting.objects.all()
    context = {
        'chatting': chatting,
    }
    return render(request, 'chatting/index.html', context)

# def new(request):
#     form = ChattingForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'chatting/new.html',context)


def create(request):
    if request.method == 'POST':
        # create
        form = ChattingForm(request.POST)
        if form.is_valid():
            chatting = form.save()
            return redirect('chatting:detail', chatting.pk)
    else:
        # new
        form = ChattingForm()
    context = {
        'form': form,
    }
    return render(request, 'chatting/create.html', context)



def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    chatting = Chatting.objects.get(pk=pk)
    context = {
        'chatting': chatting,
    }
    return render(request, 'chatting/detail.html', context)


# def delete(request, pk):
#     chatting = Chatting.objects.get(pk=pk)
#     chatting.delete()
#     return redirect('chatting:index')


# def edit(request, pk):
#     chatting = Chatting.objects.get(pk=pk)
#     context = {
#         'chatting': chatting,
#     }
#     return render(request, 'chatting/edit.html', context)


# def update(request, pk):
#     chatting = Chatting.objects.get(pk=pk)
#     chatting.title = request.POST.get('user')
#     chatting.content = request.POST.get('content')
#     chatting.save()
#     return redirect('chatting:detail', chatting.pk)