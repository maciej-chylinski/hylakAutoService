from django.contrib import admin
from .models import Post, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_date')

admin.site.register(Post)
admin.site.register(Offer, OfferAdmin)