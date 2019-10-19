from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from webapp.models import Poll, Answer, Choice



COLORS = ['red','blue','yellow','green','gray']

class StatisticsView(TemplateView):
    template_name = 'poll_templates/statistics.html'

    def get_context_data(self, **kwargs):
        context = super(StatisticsView, self).get_context_data()
        poll_pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_pk)
        answers_number = Answer.objects.filter(poll=poll).count()
        choices = Choice.objects.filter(poll=poll).annotate(num_answers=Count('answers'),
                                                            percentage_answers=Count('answers')*100/answers_number )
        context['answers_number'] = answers_number
        context['choices'] = choices
        context['colors'] = COLORS
        return context
