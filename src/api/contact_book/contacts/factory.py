import factory

from contact_book.contacts.models import Contact
from contact_book.users.factory import UserFactory


class ContactFactory(factory.django.DjangoModelFactory):
    """
        Factory class for generating test Contact data.
    """
    class Meta:
        model = Contact

    name = factory.Faker('name')
    email = factory.Sequence(lambda n: 'test-contact+%s@gmail.com' % n)
    mobile = factory.Sequence(lambda n: '+9199{:08}'.format(n))