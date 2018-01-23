import json, http.client, urllib.request, urllib.parse, urllib.error, base64

from django.core.management.base import BaseCommand

from watson_developer_cloud import AlchemyLanguageV1, WatsonException

from daback.models import Topic, TopicEntry, Article


alchemy_key = 'putkeyhere'
bing_key = 'putkeyhere'


def get_articles(topic: str):
    params = urllib.parse.urlencode({
        # Request parameters
        'q': topic,
        'count': '20',
        'offset': '0',
        'mkt': 'en-us',
        'safeSearch': 'Moderate',
    })

    try:
        conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/news/search?%s" % params, "{body}", {'Ocp-Apim-Subscription-Key': bing_key})
        response = conn.getresponse()
        data = json.loads(response.read())
        print(type(data))  # todo
        print(data)  # todo
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    print('--------------------------Returning data from Bing')
    return data['value']


def analyze_article(alchemy, targets, article) -> float:
    try:
        str_data = json.dumps(alchemy.targeted_sentiment(
            url=article['url'],
            targets=targets
        ))

        data = json.loads(str_data)

        print(article)
        print(str_data)

        score: float = 0.0
        opinions: int = 0

        for r in data['results']:
            if r['sentiment']['type'] == 'positive' or r['sentiment']['type'] == 'negative':
                score += float(r['sentiment']['score'])
                opinions += 1

        if opinions is not 0:  # i have no opinion one way or the other
            score /= opinions  # todo: better way of getting average, giving more weight if there are lots of results

        print('-----------------------------Score for %s: %f' % (targets[0], score))

        return score
    except WatsonException as e:
        # The phrase(s) were not found on the page, so Watson couldn't identify them.
        print(e)
        return 0.0
    except KeyError:
        print('Key error. JSON: ' + str_data)


def do_update():
    alchemy = AlchemyLanguageV1(api_key=alchemy_key)

    for topic in Topic.objects.all():

        positive = Article()
        negative = Article()

        highest_pos = 0.0
        lowest_neg = 0.0

        for article in get_articles(topic.name):
            targets = [topic.name]
            targets.extend(topic.synonyms.split(','))

            if targets is None:
                continue

            score = analyze_article(alchemy, targets, article)

            if score < lowest_neg:
                negative.title = article['name']
                negative.source = article['provider'][0]['name']
                negative.url = article['url']
            if score > highest_pos:
                positive.title = article['name']
                positive.source = article['provider'][0]['name']
                positive.url = article['url']

        if positive.title:
            positive.save()
        else:
            positive = None

        if negative.title:
            negative.save()
        else:
            negative = None

        entry = TopicEntry(topic=topic, article_p=positive, article_n=negative)
        entry.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        do_update()
