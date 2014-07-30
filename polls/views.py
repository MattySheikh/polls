from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import Poll

def index(request):
	latestPollList = Poll.objects.order_by('-pub_date')[:5]
	context = {'latestPollList': latestPollList}
	return render(request, 'polls/index.html', context)

def detail(request, pollID):
	poll = get_object_or_404(Poll, pk=pollID)
	return render(request, 'polls/detail.html', {'poll': poll})

def results(request, pollID):
	return HttpResponse("You're looking at the results of poll %s" % pollID)

def vote(request, pollID):
	return HttpResponse("You're voting on poll %s" % pollID)