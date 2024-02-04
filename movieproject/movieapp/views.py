from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MovieForms, SearchForm
from .models import Movie, Category
from django.contrib import messages


# Create your views here.@login_required(login_url='credentials/register')

def index(request):
    category = request.GET.get('category')
    if category == None:
        movie = Movie.objects.all()
    else:
        movie = Movie.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {
        'movie_list': movie,
        'categories': categories
    }
    return render(request, "index.html", context)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "details.html", {'movie': movie})


@login_required(login_url='credentials:login')
def add_movie(request):
    form = MovieForms()

    if request.method == 'POST':
        form = MovieForms(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            return redirect('/')
    else:
        form = MovieForms()

    context = {
        "form": form
    }

    return render(request, 'add.html', context)

@login_required(login_url='credentials:login')
def update(request, id):
    movie = Movie.objects.get(id=id)
    categories = Category.objects.all()
    if request.user == movie.added_by:
        form = MovieForms(request.POST or None, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'edit.html', {'form': form, 'movie': movie})
    else:
        messages.error(request,'Your are not authorised to update it')
        return redirect('movieapp:details',movie_id=id)
    
    return render(request,'edit.html',{'movie':movie,'categories':categories})


@login_required(login_url='credentials:login')
def delete(request, id):
    movie = Movie.objects.get(id=id)
    if request.user == movie.added_by:
        movie.delete()
        return redirect('/')
    else:
        messages.error(request,'Your are not authorised to update it')
        return redirect('movieapp:details',movie_id=id)
    return render(request, 'delete.html')


def search_movies(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Perform search logic, for example:
            results = Movie.objects.filter(movie_name__icontains=query)
            return render(request, 'search_results.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form})
