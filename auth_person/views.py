from django.shortcuts import render

# Create your views here.
from auth_person.forms import PersonRegistrationForms
from auth_person.func import create_new_user
from auth_person.models import Person, Role, Logo


def registration(request):
    if request.method == 'POST':
        new_person = PersonRegistrationForms(request.POST, request.FILES)
        if new_person.is_valid():
            new_user = create_new_user(request)
            return render(request, 'personalArea.html', {'person': new_user, 'logo_obj': new_user.logoId.logo.url})
        else:
            return render(request, 'invData.html')
    else:
        new_person = PersonRegistrationForms()
        return render(request, 'registration.html', {'form': new_person})


def sign(request):
    if request.method == 'POST':
        pass



def is_sign(request):
    pass
