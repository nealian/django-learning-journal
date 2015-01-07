from django.contrib import admin
from journal.models import Entry, Tag

class TagInline(admin.TabularInline):
    model = Tag.entries.through
    extra = 1

class TagAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]
    exclude = ('entries',)

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Entry fields', {'fields': ['title','contents']}),
        ('Publishing',   {'fields': ['public']}),
    ]
    inlines = [
        TagInline,
    ]
    list_display = ('title', 'pub_date', 'mod_date', 'public')
    list_filter = ['pub_date', 'mod_date']
    search_fields = ['title']
    date_hierarchy = 'pub_date'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
            obj.modifier = request.user
        else if change:
            obj.modifier = request.user
        obj.save()

admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag, TagAdmin)
