from django.shortcuts import render , redirect
from eithers.forms import CommentForm, QuestionForm

from eithers.models import Question
from .models import Question , Comment
import random as random1
# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions' : questions,
    }
    return render(request,'eithers/index.html',context)

def create(request):
    # issue_a = request.POST.get('RED_TEAM')
    # issue_b = request.POST.get('BLUE_TEAM')
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('eithers:detail',question.pk)
    else:
        form = QuestionForm()
    context = {
        'form' : form,
    }
    return render(request,'eithers/create.html',context)

def detail(request,pk):
    question = Question.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = question.comment_set.all()
    context = {
        'question':question,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request,'eithers/detail.html',context)


def comments_create(request,pk):
    question = Question.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question = question
        comment.save()
    return redirect('eithers:detail',question.pk)

def random(request):
    question = random1.choice(Question.objects.all())
    return redirect('eithers:detail', question.pk)