"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import home


def generate_api_url_include(name):
    regex = r'^{}/'.format(name)
    to_include = include('contact_book.{}.urls'.format(name))
    namespace = 'contact_book.{}'.format(name)
    return url(regex, to_include, name=namespace)


api_namespaces_to_include = [
    "users",
    "contacts",
]

api_namespaced_urls = [
    generate_api_url_include(name) for name in api_namespaces_to_include
]


urlpatterns = [
    url(r'^api/v1/', include([
        url(r'', include(api_namespaced_urls)),
        url(r'^$', home, name='home'),
    ],
    ))
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path('_admin/', admin.site.urls),
]

