from auth_person.models import Person, Role, Logo


def create_new_user(request):
    new_user = Person()
    new_role = Role()
    new_logo = Logo()
    new_user.login = request.POST.get('login')
    new_user.password = request.POST.get('password')
    new_user.name = request.POST.get('name')
    new_user.surname = request.POST.get('surname')
    new_user.birthday = request.POST.get('birthday')
    new_user.balance = 0.0
    new_role.role = 'user'
    new_role.save()
    new_logo.logo = request.FILES.get('logo')
    new_logo.save()
    new_user.roleId = new_role
    new_user.logoId = new_logo
    new_user.save()
    return new_user


