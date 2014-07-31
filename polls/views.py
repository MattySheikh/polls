from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Poll, Choice

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latestPollList'
	def get_queryset(self):
		"""Return the last five published polls"""
		return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Poll
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Poll
	template_name = 'polls/results.html'

def vote(request, pollID):
	poll = get_object_or_404(Poll, pk=pollID)
	try:
		selectedChoice = poll.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'poll': poll,
			'errorMessage': "You didn't select a choice."
		})
	else:
		selectedChoice.votes += 1
		selectedChoice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))