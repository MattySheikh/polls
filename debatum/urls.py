from django.conf.urls import patterns, include, url
from polls import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	# ex: /polls/
	url(r'^polls/$', views.index),
	# ex: /polls/5/
    url(r'^polls/(?P<PollID>\d+)/$', views.detail),
	# ex: /polls/5/results/
	url(r'^polls/(?P<pollID>\d+)/results/$', views.results),
	# ex: /polls/5/vote/
	url(r'^polls/(?P<pollID>\d+)/vote/$', views.vote),
)
