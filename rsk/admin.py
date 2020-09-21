from django.contrib import admin
from rsk import models


class TopicAdminView(admin.ModelAdmin):
    list_display=('topic_name',)
    search_fields=('topic_name',)
class WebpageAdminView(admin.ModelAdmin):
    list_display=('topic','name','url')
    search_fields=('topic','name')
    list_editable=('name',)
    list_filter=('topic',)
class AccesDetailsAdminView(admin.ModelAdmin):
    list_display=('webpage','datetime')
    search_fields=('webpage','datetime')
admin.site.register(models.Topic,TopicAdminView)
admin.site.register(models.Webpage,WebpageAdminView)
admin.site.register(models.AccesDetails,AccesDetailsAdminView)
admin.site.register(models.ProfilePic)