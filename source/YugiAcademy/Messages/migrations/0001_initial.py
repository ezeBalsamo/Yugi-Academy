# Generated by Django 4.1 on 2022-09-27 22:48

import Messages.messages.message
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time_sent', models.DateTimeField()),
                ('content', models.TextField()),
                ('receiver', models.ForeignKey(on_delete=models.SET(Messages.messages.message.deleted_user), related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=models.SET(Messages.messages.message.deleted_user), related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
