from django.contrib import admin
from .models import Language, StudentExperience, TutorialSeries, Lesson
# Register your models here.

class LanguageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",),}

	list_display = ("name","active", )

admin.site.register(Language, LanguageAdmin)

class TutorialSeriesAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",),}
	list_display = ("name", "archived",)

admin.site.register(TutorialSeries,TutorialSeriesAdmin) 


class LessonAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("title",),}
	list_display = ("title", "active","free_preview",)


admin.site.register(Lesson, LessonAdmin)


admin.site.register(StudentExperience)
