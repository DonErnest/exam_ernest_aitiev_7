from django.urls import reverse
from django.views.generic import ListView, RedirectView, DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import PollForm
from webapp.models import Poll


class PollListRedirect(RedirectView):
    pattern_name = 'list polls'


class PollListView(ListView):
    model = Poll
    context_object_name = 'polls'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1
    template_name = 'poll_templates/poll_list.html'


class PollDetailedView(DetailView):
    model = Poll
    context_object_name = 'poll'
    template_name = 'poll_templates/poll_detailed.html'


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'poll_templates/poll_create.html'

    def get_success_url(self):
        return reverse('view poll', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    form_class = PollForm
    template_name = 'poll_templates/poll_update.html'

    def get_success_url(self):
        return reverse('view poll', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'poll_templates/poll_delete.html'
    success_url = 'index'


