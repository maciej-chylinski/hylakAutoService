from django.contrib import admin
from .models import Post, Offer, Contact


class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'created_date')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_title', 'contact_name', 'phone', 'address', 'email')


admin.site.register(Post)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Contact)