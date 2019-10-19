from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView, CreateView

from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class ChoiceCreateView(CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choice_templates/choice_create.html'

    def dispatch(self, request, *args, **kwargs):
        self.poll = self.get_poll()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.poll.choices.create(**form.cleaned_data)
        return redirect('view poll', pk=self.poll.pk)

    def get_poll(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)

    def get_success_url(self):
        return reverse('view poll', kwargs={'pk': self.object.poll.pk})

class ChoiceUpdateView(UpdateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choice_templates/choice_update.html'

    def get_success_url(self):
        return reverse('view poll', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice_templates/choice_delete.html'

    def get_success_url(self):
        return reverse('view poll', kwargs={'pk': self.object.poll.pk})

    