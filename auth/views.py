from django.shortcuts import render

# Create your views here.

def registration(request):
    """    if request.method == 'POST':
        new_person = PersonRegistrationForms(request.POST)
        if new_person.is_valid():
            new_user = Person()
            new_role = Role()
            new_user.login = request.POST.get('login')
            new_user.password = request.POST.get('password')
            new_user.name = request.POST.get('name')
            new_user.surname = request.POST.get('surname')
            new_user.birthday = request.POST.get('birthday')
            new_user.balance = 0.0
            new_role.role = 'user'
            new_role.save()
            new_user.roleId = new_role
            new_user.save()
            return render(request, 'personalArea.html', {'person': new_user})
        else:
            return render(request, 'invData.html')
    else:
        new_person = PersonRegistrationForms()
        return render(request, 'registration.html', {'form': new_person})"""


def sign(request):
    pass


def is_sign(request):
    pass
