# Create your views here.
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response,get_object_or_404,get_list_or_404
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Poll

def index(request):
	# e.g. (1)
	# return HttpResponse("Hello, world. You're at the poll index.")

	# e.g. (2)
	# latest_poll_list = Poll.objects.all().order_by('-pub_date')
	# output = '<br />'.join([p.question for p in latest_poll_list])
	# return HttpResponse(output)

	# e.g. (3) use Django's template
	# latest_poll_list = Poll.objects.all()
	# t = loader.get_template('polls/index.html')
	# c = Context({
	# 	'latest_poll_list':latest_poll_list,
	# })
	# return HttpResponse(t.render(c))

	#e.g. (4) A shortcut: render_to_response()
	# latest_poll_list = Poll.objects.all().order_by('-pub_date')[:3]
	latest_poll_list = get_list_or_404(Poll)
	return render_to_response('polls/index.html',{'latest_poll_list':latest_poll_list})


def detail(request,poll_id):
	# e.g. (1)
	# return HttpResponse("You're looking at poll %s." % poll_id)

	# e.g. (2)
	# try:
	# 	p = Poll.objects.get(id=poll_id)
	# except:
	# 	raise Http404
	# return render_to_response('polls/detail.html',{'poll':p})

	# e.g. (3) It's a very common way to use get() and raise Http404 if the object doesn't exist
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('polls/detail.html',{'poll':p},
								context_instance=RequestContext(request))	

def results(request, poll_id):
	# return HttpResponse("You're looking at the results of poll %s." % poll_id)
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('polls/results.html', {'poll':p})

def vote(request, poll_id):
	# return HttpResponse("You're voting on poll %s." % poll_id)

	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except:
		return render_to_response('polls/detail.html',{
			'poll':p,
			'error_message':"You didn't select a choice.",
		}, context_instance=RequestContext(request))
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a 
		# user hits the Back button.
		# return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
		return HttpResponseRedirect('/polls/%s/results' % p.id)  # as same as above line
