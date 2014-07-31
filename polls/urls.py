from django.conf.urls import patterns, include, url
from polls import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	# ex: /polls/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	# ex: /polls/5/results/
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	# ex: /polls/5/vote/
	url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'),
)
