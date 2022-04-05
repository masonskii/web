from auth_person.models import Person, PersonName, PersonCard


def search_person(number_card):
    card = PersonCard.objects.get(number=number_card)
    user = Person.objects.get(card=card.card_id)
    if not user is None:
        return user


def sender(request_user):
    person = Person.objects.get(person_id=request_user.id)
    if not person:
        return None
    else:
        return person
