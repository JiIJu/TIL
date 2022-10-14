from django.shortcuts import render , redirect , get_object_or_404
from .models import Movie , Comment
from .forms import MovieForm , CommentForm

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('pk')
    context = {
        'movies' : movies,
    }
    return render(request,'movies/index.html',context)

def create(request):
    if  request.method =='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user_id = request.user
            movie.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request , 'movies/create.html',context)

def detail(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie' : movie,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request,'movies/detail.html',context)

def delete(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    if request.user.is_authenticate:
        if request.user == movie.user_id:
            movie.delete()
            return redirect('movies:index')
    return redirect('movies:detail',movie.pk)

def update(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    if request.user == movie.user_id:
        if request.method =='POST':
            form = MovieForm(request.POST , instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail',movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:index')
    context = {
        'movie':movie,
        'form' : form,
    }
    return render(request,'movies/update.html',context)


def comments_create(request,pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie,pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user_id = request.user
            comment.movie_id = movie
            comment.save()
        return redirect('movies:detail',movie.pk)
    return redirect('accounts:login')


def comments_delete(request,movie_pk,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment,pk=comment_pk)
        if request.user == comment.user_id:
            comment.delete()
    return redirect('movies:detail',movie_pk)
