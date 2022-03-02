from django.shortcuts import render

# Create your views here.
from auth_person.forms import PersonRegistrationForms, SignIn
from auth_person.func import create_new_user
from auth_person.models import Person, Role, Logo


def registration(request):
    if request.method == 'POST':
        new_person = PersonRegistrationForms(request.POST, request.FILES)
        if new_person.is_valid():
            new_user = create_new_user(request)
            return render(request, 'main.html')
        else:
            return render(request, 'invData.html')
    else:
        new_person = PersonRegistrationForms()
        return render(request, 'registration.html', {'form': new_person})


def signUp(request):
    if request.method == 'POST':
        new_session_sign = SignIn(request.POST)
        if new_session_sign.is_valid():
            user_login, user_password = request.POST.get('login'), request.POST.get('password')
            session_complited = Person.objects.get(login=user_login, password=user_password)
            if session_complited is None:
                return render(request, 'invData.html')
            else:
                return render(request, 'personalArea.html', {'person': session_complited,
                                                             'logo_obj': session_complited.logoId.logo.url})
        else:
            return render(request, 'invData.html')
    else:
        form_sign = SignIn()
        return render(request, 'sign.html', {'form': form_sign})




def is_sign(request):
    pass
