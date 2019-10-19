from django.contrib import admin

from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_at']
    list_filter = ['created_at']
    search_fields = ['question']
    fields = ['question', 'created_at']
    readonly_fields = ['created_at']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['answer_version','poll']
    list_filter = ['poll']
    search_fields = ['poll']
    fields = ['answer_version','poll']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer)