import factory

from contact_book.users.models import User

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Sequence(lambda n: 'test-contactholder+%s@gmail.com' % n)
    password = 'password'
    is_active = True

