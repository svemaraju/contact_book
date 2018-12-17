from django.contrib import admin

from contact_book.contacts.models import Contact

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'holder',)
	search_fields = ('name', 'email',)

admin.site.register(Contact, ContactAdmin)