from django.contrib import admin

from contact_book.users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name',)
    search_fields = ('email','id',)

admin.site.register(User, UserAdmin)
