from django.contrib import admin
from journal.models import Entry, Tag

class TagInline(admin.TabularInline):
    model = Tag.entries.through
    extra = 0

class TagAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]
    exclude = ('entries',)

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Entry fields',     {'fields': ['title','contents']}),
        ('Date information', {'fields': ['pub_date','mod_date'], 'classes': ['collapse']}),
    ]
    inlines = [
        TagInline,
    ]

admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag, TagAdmin)
