from django.shortcuts import render
from .models import SaveGotham, HeroesAlliance
from django.shortcuts import get_object_or_404
from .forms import BatmanForm

# Create your views here.
def batman(request):
    batmen = SaveGotham.objects.all()
    return render(request, 'batman/im_batman.html', {'batmen': batmen})

def weapon_details(request, batman_id):
    weapon = get_object_or_404(SaveGotham, pk=batman_id)
    return render(request, 'batman/weapon_details.html', {'weapon': weapon})


#forms
def villians_view(request):
    villians = None
    if request.method == 'POST': # if the form has been submitted...
        form = BatmanForm(request.POST)
        if form.is_valid():
            hero = form.cleaned_data['name']
            alliances = HeroesAlliance.objects.filter(heroes=hero)
            villians = [alliance.villian for alliance in alliances]  #For each 'alliance' in alliances, it gets the villian attribute.
    else: # if the form has not been submitted...
        form = BatmanForm()
    return render(request, 'batman/villains.html', {'villians': villians, 'form': form})