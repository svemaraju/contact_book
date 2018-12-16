from django.contrib import admin

from contact_book.contacts.models import Contact

class ContactAdmin(admin.ModelAdmin):
	pass

admin.site.register(Contact, ContactAdmin)