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

    return render(request, 'myapp/details.html', {'hero': superhero})

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
    selected_hero = Superhero.objects.get(pk=hero_id)
    if request.method == "POST":
        selected_hero.name = request.POST.get('name')
        selected_hero.alter_ego_name = request.POST.get('alter_ego_name')
        selected_hero.primary_super_ability = request.POST.get('primary_super_ability')
        selected_hero.secondary_super_ability = request.POST.get('secondary_super_ability')
        selected_hero.catchphrase = request.POST.get('catchphrase')
        selected_hero.save()
        context = {
            "selected_hero": selected_hero
        }
        return render(request, 'superhero/detail.html', context)
    else:
        context = {
            "selected_hero": selected_hero
        }
        return render(request, 'superhero/edit.html', context)

def delete(request, hero_id):
    selected_hero = Superhero.objects.get(pk=hero_id)
    if request.method == "POST":
        selected_hero.delete()
        return index(request)
    else:
        context = {
            "selected_hero": selected_hero
        }
        return render(request, 'superhero/delete.html', context)
