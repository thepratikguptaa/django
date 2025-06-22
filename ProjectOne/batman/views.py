from django.shortcuts import render
from .models import SaveGotham

# Create your views here.
def batman(request):
    batmen = SaveGotham.objects.all()
    return render(request, 'batman/im_batman.html', {'batmen': batmen})