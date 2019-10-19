# Generated by Django 2.2 on 2019-10-19 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_poll_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время ответа')),
                ('answer_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='webapp.Choice', verbose_name='Вариант ответа')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='webapp.Poll', verbose_name='Опрос')),
            ],
        ),
    ]
