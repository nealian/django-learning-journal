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
    list_display = ('title', 'author', 'pub_date', 'modifier', 'mod_date', 'public')
    list_filter = ['pub_date', 'mod_date']
    search_fields = ['title']
    date_hierarchy = 'pub_date'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
            obj.modifier = request.user
        elif change:
            obj.modifier = request.user
        obj.save()

    def queryset(self, request):
        qs = super(EntryAdmin, self).queryset(request)
        if request.user.has_perm('journal.entry_edit_others'):
            return qs
        else:
            return qs.filter(author=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        if request.user.has_perm('journal.entry_edit_others') or obj.author == request.user:
            return True
        else:
            return False

    has_delete_permission = has_change_permission

admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag, TagAdmin)
