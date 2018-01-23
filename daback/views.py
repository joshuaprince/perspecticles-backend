import random

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Topic, TopicEntry


def get_topic(request, topic_str: str):
    topic: Topic = get_object_or_404(Topic, name__iexact=topic_str)

    latest_entry: TopicEntry = TopicEntry.objects.filter(topic=topic).order_by('-time')[0]

    resp = {'success': True, 'response_version': 1, 'topic': topic.name, 'articles': {}}

    if latest_entry.article_p and latest_entry.article_p.title:
        resp['articles']['positive'] = {'url': latest_entry.article_p.url, 'title': latest_entry.article_p.title,
                                        'source': latest_entry.article_p.source}

    if latest_entry.article_n and latest_entry.article_n.title:
        resp['articles']['negative'] = {'url': latest_entry.article_n.url, 'title': latest_entry.article_n.title,
                                        'source': latest_entry.article_n.source}

    return JsonResponse(resp)


def get_list(request):
    entries = list(TopicEntry.objects.all().order_by('-time')[0:Topic.objects.count()])
    random.shuffle(entries)

    return render(request, template_name='daback/list.html', context={
        'topic_entries': entries
    })


def get_topics(request):
    return JsonResponse({'success': True, 'response_version': 1,
                         'topics': [str(i) for i in Topic.objects.values_list('name', flat=True)]})
