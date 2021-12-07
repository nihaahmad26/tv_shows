from django.shortcuts import render, redirect
from .models import Show

def index(request):
    context = {
        'all_shows':Show.objects.all()
    }
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')

def create(request):
    Show.objects.create(title=request.POST['title'], network=request.POST['network'],release=request.POST['release'], description=request.POST['description'])
    return redirect('/')

def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show':one_show
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    to_update = Show.objects.get(id=show_id)
    to_update.title = request.POST['title']
    to_update.release_date = request.POST['release_date']
    to_update.network = request.POST['network']
    to_update.description = request.POST['description']
    to_update.save()

    return redirect('/')

def show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'show.html', context)

def delete(request, show_id):
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/')