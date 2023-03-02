from django.contrib import admin
from .models import (
    Vocabulary, Entries,
    Definitions, Examples,
    Synonyms, Tables
)

class TablesAdmin(admin.ModelAdmin):
    list_display = ('tableName',)
    fields = ('tableName', 'word')

class EntriesAdmin(admin.ModelAdmin):
    list_display = ('word', 'lexicalCategory',)

class DefinitionsAdmin(admin.ModelAdmin):
    list_display = ('word', 'entry', 'definition')

class ExamplesAdmin(admin.ModelAdmin):
    list_display = ('word', 'entry', 'example')

class SynonymsAdmin(admin.ModelAdmin):
    list_display = ('word', 'entry', 'synonym')

# Register your models here.
admin.site.register(Vocabulary)
admin.site.register(Tables, TablesAdmin)
admin.site.register(Entries, EntriesAdmin)
admin.site.register(Definitions, DefinitionsAdmin)
admin.site.register(Examples, ExamplesAdmin)
admin.site.register(Synonyms, SynonymsAdmin)