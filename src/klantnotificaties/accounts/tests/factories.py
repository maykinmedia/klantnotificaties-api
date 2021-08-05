import factory

from rest_framework.authtoken.models import Token

from ..models import User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User


class TokenFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Token
