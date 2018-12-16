from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView
)
from rest_framework import status
from rest_framework.response import Response

from contact_book.contacts.models import Contact
from contact_book.contacts.serializers import ContactSerializer

class ContactAPI(ListCreateAPIView):
    serializer_class = ContactSerializer
    
    def get_queryset(self):
        return Contact.objects.filter(holder=self.request.user)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = self.serializer_class(data=data)
        serializer.initial_data['holder'] = request.user.id
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()
        return Response(ContactSerializer(contact).data, status=status.HTTP_200_OK)