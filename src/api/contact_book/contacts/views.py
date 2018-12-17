from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView
)
from rest_framework import status
from rest_framework.response import Response

from contact_book.contacts.filters import ContactSearchFilter
from contact_book.contacts.models import Contact
from contact_book.contacts.serializers import ContactSerializer

class ContactAPI(ListCreateAPIView):
    serializer_class = ContactSerializer
    filter_backends = (ContactSearchFilter,)
    
    def get_queryset(self):
        return Contact.objects.filter(holder=self.request.user).order_by('name')

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = self.serializer_class(data=data)
        serializer.initial_data['holder'] = request.user.id
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()
        return Response(ContactSerializer(contact).data, status=status.HTTP_200_OK)


class ContactDetailAPI(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer

    def get_object(self):
        contact = get_object_or_404(Contact, pk=self.kwargs['pk'])
        return contact