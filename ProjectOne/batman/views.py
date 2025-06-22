from django.shortcuts import render
from .models import SaveGotham
from django.shortcuts import get_object_or_404

# Create your views here.
def batman(request):
    batmen = SaveGotham.objects.all()
    return render(request, 'batman/im_batman.html', {'batmen': batmen})

def weapon_details(request, batman_id):
    weapon = get_object_or_404(SaveGotham, pk=batman_id)
    return render(request, 'batman/weapon_details.html', {'weapon': weapon})