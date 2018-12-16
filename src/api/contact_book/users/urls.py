from django.conf.urls import url

from contact_book.users.views import (
		Register,
		SignIn,
		Logout,
	)

namespace_prefix = 'contact_book.users.'

urlpatterns = [
    url(r'^register/$', Register.as_view(),
        name=namespace_prefix + "register"),

    url(r'^signin/$', SignIn.as_view(),
        name=namespace_prefix + "signin"),

    url(r'^logout/$', Logout.as_view(),
        name=namespace_prefix + "logout"),
]