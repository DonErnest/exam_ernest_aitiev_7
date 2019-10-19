from django import forms

from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ['question']
        labels = {'question': 'Вопрос'}


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields=['answer_version']
        labels={'answer_version': 'Вариант ответа'}