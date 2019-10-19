from django import forms

from webapp.models import Poll, Choice, Answer


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


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields=['answer_choice']
        labels={'answer_choice':'Вариант ответа'}
