from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import AnswerForm
from webapp.models import Answer, Poll, Choice


class AnswerGiveView(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'answer_templates/answer_add.html'

    def get_context_data(self, **kwargs):
        context = super(AnswerGiveView, self).get_context_data()
        context['form'].fields['answer_choice'].queryset = Choice.objects.filter(poll=self.get_poll())
        context['poll'] = self.get_poll()
        return context

    def dispatch(self, request, *args, **kwargs):
        self.poll = self.get_poll()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.poll.answers.create(**form.cleaned_data)
        return redirect('view poll', pk=self.poll.pk)

    def get_poll(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)

    def get_success_url(self):
        return reverse('view poll', kwargs={'pk': self.object.poll.pk})