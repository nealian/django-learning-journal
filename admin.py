from django.contrib import admin
from journal.models import Entry, Tag
from django.utils import timezone

class TagInline(admin.TabularInline):
    model = Tag.entries.through
    extra = 0

class TagAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]
    exclude = ('entries',)

class EntryAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]
    list_display = ('title', 'author', 'pub_date', 'modifier', 'mod_date', 'public')
    list_filter = ('pub_date', 'mod_date',)
    search_fields = ('title',)
    date_hierarchy = 'pub_date'
    actions = ('entry_publish', 'entry_unpublish')
    fieldsets = (
        (None,             {'fields': ('title','contents',)}),
        ('Post meta-info', {'fields': (('create_date', 'mod_date', 'pub_date',), ('author', 'modifier', 'publisher',),), 'classes': ('collapse',)}),
    )
    readonly_fields = ('pub_date', 'mod_date', 'author', 'modifier',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(EntryAdmin, self).get_fieldsets(request, obj)
        if request.user.has_perm('journal.entry_publish'):
            fieldsets += (('Publishing', {'fields': ('public',)}),)
        return fieldsets
 
    def get_actions(self, request):
        actions = super(EntryAdmin, self).get_actions(request)
        if not request.user.has_perm('journal.entry_publish'):
            if 'entry_publish' in actions:
                del actions['entry_publish']
            if 'entry_unpublish' in actions:
                del actions['entry_unpublish']
        return actions

    def entry_publish(self, request, queryset):
        rows_updated = queryset.filter(public=False).update(public=True, pub_date=timezone.now(), publisher=request.user)
        rows_untouched = queryset.count() - rows_updated
        update_message_bit = '1 entry was' if rows_updated == 1 else "%s entries were" % rows_updated
        untouched_message_bit = '1 selected entry was' if rows_untouched == 1 else "%s selected entries were" % rows_untouched
        message = "{} successfully published ({} already published)".format(update_message_bit, untouched_message_bit) if rows_untouched else "{} successfully published".format(update_message_bit)
        self.message_user(request, message)
    entry_publish.short_description = "Publish selected entries"

    def entry_unpublish(self, request, queryset):
        rows_updated = queryset.update(public=False)
        message_bit = '1 entry was' if rows_updated == 1 else "%s entries were" % rows_updated
        self.message_user(request, "%s successfully unmarked public." % message_bit)
    entry_unpublish.short_description = "Unpublish selected entries"

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
