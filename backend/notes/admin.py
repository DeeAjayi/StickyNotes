from django.contrib import admin

from .models import Notes


class NotesAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'time_stamp', 'is_public')


admin.site.register(Notes, NotesAdmin)
