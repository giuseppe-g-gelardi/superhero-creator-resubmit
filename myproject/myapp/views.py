from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superheroes
# Create your views here.


def index(request):
    all_superheroes = Superheroes.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'myapp/index.html', context)

def detail(request, superhero_id):
    superhero = Superheroes.objects.get(pk=superhero_id)
    context = {
        'superhero': superhero
    }

    return render(request, 'myapp/details.html', context)

def create(request):
    if request.method == 'POST':
        superhero_name = request.POST.get('name')
        alter_ego_name = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catch_phrase = request.POST.get('catchphrase')
        new_superhero = Superheroes(
            superhero_name = superhero_name, 
            alter_ego_name = alter_ego_name, 
            primary_ability = primary_ability, 
            secondary_ability = secondary_ability, 
            catch_phrase = catch_phrase
        )
        new_superhero.save()
        return HttpResponseRedirect(reverse('myapp:index'))
    else:
        return render(request, 'myapp/create.html')

def edit(request, superhero_id):
    superhero = Superheroes.objects.get(pk=superhero_id)
    if request.method == "POST":
        superhero.superhero_name = request.POST.get('name')
        superhero.alter_ego_name = request.POST.get('alter_ego')
        superhero.primary_ability = request.POST.get('primary_ability')
        superhero.secondary_ability = request.POST.get('secondary_ability')
        superhero.catchphrase = request.POST.get('catchphrase')
        superhero.save()
        context = {
            "superhero": superhero
        }
        return render(request, 'myapp/details.html', context)
    else:
        context = {
            "superhero": superhero
        }
        return render(request, 'myapp/edit.html', context)

def delete(request, superhero_id):
    superhero = Superheroes.objects.get(pk=superhero_id)
    if request.method == "POST":
        superhero.delete()
        return index(request)
    else:
        context = {
            "superhero": superhero
        }
        return render(request, 'myapp/delete.html', context)
