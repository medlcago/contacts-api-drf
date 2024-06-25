from django.contrib import admin

from apps.contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone_number", "user")
    list_display_links = ("id", "name")
