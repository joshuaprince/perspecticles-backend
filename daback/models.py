from django.db import models


class Article(models.Model):
    """
    Represents an article... who would have guessed
    """
    title = models.CharField(max_length=512, unique=False)
    source = models.CharField(max_length=128, unique=False)
    url = models.URLField()

    def __str__(self):
        return self.source + ': '+ self.title


class Topic(models.Model):
    """
    Represents a single topic - there should be no duplicates.
    To delete, set deleted to true. Don't delete the entry from SQL when any TopicEntries rely on it.
    """
    name = models.CharField(max_length=64, unique=True)
    synonyms = models.CharField(max_length=512, default='', blank=True)  # Delimited by commas

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TopicEntry(models.Model):
    """
    A single response to a topic. When the server is queried, we return data from the latest TopicEntry
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    time = models.DateTimeField(auto_now=True)

    article_p = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_p', null=True)
    article_n = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_n', null=True)

    def __str__(self):
        return self.topic.name + ' :: ' + str(self.time)

    class Meta:
        verbose_name_plural = 'Topic Entries'
