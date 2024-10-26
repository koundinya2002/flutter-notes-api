from django.contrib import admin
from .models import Note

# Register your models here.
# class NoteAdmin(admin.ModelAdmin):
#     list_display = ("body","updated")
#     prepopulated_fields = {"slug": ("updated")}

admin.site.register(Note)