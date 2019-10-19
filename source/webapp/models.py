from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.question


class Choice(models.Model):
    answer_version = models.TextField(max_length=300, null=False, blank=False, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll',on_delete=models.CASCADE, related_name='choices', verbose_name='Опрос')

    def __str__(self):
        return self.answer_version


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='answers', verbose_name='Опрос')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время ответа')
    answer_choice = models.ForeignKey('webapp.Choice', on_delete=models.CASCADE, related_name='answers', verbose_name='Вариант ответа')
