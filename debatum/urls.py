from django.conf.urls import patterns, include, url
from polls import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^polls/$', views.index, name='index'),
	# ex: /polls/5/
    url(r'^polls/(?P<poll_id>\d+)/$', views.detail, name='detail'),
	# ex: /polls/5/results/
	url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
	# ex: /polls/5/vote/
	url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)
