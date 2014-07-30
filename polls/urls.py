from django.conf.urls import patterns, include, url
from polls import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index),
	# ex: /polls/5/
    url(r'^(?P<pollID>\d+)/$', views.detail, name='detail'),
	# ex: /polls/5/results/
	url(r'^(?P<pollID>\d+)/results/$', views.results, name='results'),
	# ex: /polls/5/vote/
	url(r'^(?P<pollID>\d+)/vote/$', views.vote, name='vote'),
)
