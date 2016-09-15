from django.shortcuts import render, get_object_or_404, reverse

from django.http import HttpResponse, HttpResponseRedirect

# not needed when using shortcut
# from django.template import loader, RequestContext

from .models import Question
# Create your views here.

def index(request):
  latest_questions = Question.objects.order_by('-pub_date')[:5]
  
#  template = loader.get_template('polls/index.html')
#  context = RequestContext(request, {
#    'latest_questions': latest_questions
#  })
  
#  output = ", ".join(q.question_text for q in latest_questions)
#  return HttpResponse(template.render(context))

# shortcut
  context = {'latest_questions':latest_questions}
  return render(request, 'polls/index.html', context)
  
def detail(request, question_id):
#  question = Question.objects.get(pk=question_id)

  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})
  
#  return HttpResponse("This is the detail view of the question: %s" % question_id)
  
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})


#  return HttpResponse("These are the results of the question: %s" % question_id)
  
def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk = request.POST['choice'])
  except:
    return render(request, 'polls/detail.html', {'question': question, 'error_message':"Please select a choice"})
    
    # try worked
  else:    
    selected_choice.votes += 1
    selected_choice.save()
    
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#  return HttpResponse("Votes on question: %s" % question_id)
