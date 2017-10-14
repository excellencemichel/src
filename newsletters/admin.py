from django.contrib import admin
from .models import NewsletterUser

# Register your models here.

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ("email", "date_added","id",)






admin.site.register(NewsletterUser, NewsletterAdmin)
