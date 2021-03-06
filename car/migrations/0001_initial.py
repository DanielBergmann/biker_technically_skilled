# Generated by Django 2.0.13 on 2019-06-02 10:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('last_added_text', models.TextField()),
                ('first_added_text_or_name', models.TextField()),
                ('finished', models.BooleanField()),
                ('contributors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
