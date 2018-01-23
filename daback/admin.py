from django.contrib import admin

from .models import Topic, TopicEntry, Article

admin.site.register(Topic)
admin.site.register(TopicEntry)
admin.site.register(Article)

# Register your models here.
