from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll

def index(request):
	latestPollList = Poll.objects.order_by('-pub_date')[:5]
	output = ', '.join([p.question for p in latestPollList])
	return HttpResponse(output)

def detail(request, pollID):
	return HttpResponse("You're looking at poll %s." % pollID)

def results(request, pollID):
	return HttpResponse("You're looking at the results of poll %s" % pollID)

def vote(request, pollID):
	return HttpResponse("You're voting on poll %s" % pollID)