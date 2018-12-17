from django.conf.urls import url

from contact_book.contacts.views import ContactAPI, ContactDetailAPI

namespace_prefix = 'contact_book.contacts.'

urlpatterns = [
    url(r'^$', ContactAPI.as_view(),
        name=namespace_prefix),
    url(r'^(?P<pk>\d+)/$', ContactDetailAPI.as_view(),
        name=namespace_prefix + "detail"),
]