from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_topics),
    url(r'(?P<topic_str>.*)/', views.get_topic),
]
