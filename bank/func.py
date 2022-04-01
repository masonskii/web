from auth_person.models import Person


def search_person(name, number_card):
    user = Person.objects.get(name=name.name, card__number=number_card)
    if not user:
        return None
    else:
        return user


def sender(request_user):
    person = Person.objects.get(login=request_user.username)
    if not person:
        return None
    else:
        return person
