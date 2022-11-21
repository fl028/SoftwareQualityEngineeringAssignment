from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Employee
from .forms import NameForm

class IndexView(generic.ListView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['no_questions'] = "No questions!"
        context['latest_question_list'] = Question.objects.all()
        return context

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('apps.demo_app:results', args=(question.id,)))



def name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            name = form.cleaned_data['your_name']
            return render(request, 'display-name.html',  {'name': name})

    # if a GET (or any other method) we'll create a blank form
    else:
        query = request.GET.get('query')
        form = NameForm(initial={'your_name': query})
        return render(request, 'name.html', {'form': form, 'query': query})


class EmployeeView(generic.ListView):
    template_name = 'employees.html'
    context_object_name = 'employees_list'

    def get_queryset(self):
        return Employee.objects.all()