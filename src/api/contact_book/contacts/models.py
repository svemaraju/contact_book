from django.db import models

from contact_book.models import TimestampedModel
from contact_book.users.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Contact(TimestampedModel):
    """
        Represents a contact within the Contact Book App.
    """
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255)
    mobile = PhoneNumberField(blank=True)

    # holder of the contact
    holder = models.ForeignKey('users.User', on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        unique_together = (("holder", "email"),)