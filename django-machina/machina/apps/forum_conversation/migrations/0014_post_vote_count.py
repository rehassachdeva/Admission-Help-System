# Generated by Django 2.0.3 on 2018-04-08 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_conversation', '0013_post_upvoters'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vote_count',
            field=models.PositiveIntegerField(blank=True, default=0, editable=False, verbose_name='Vote count'),
        ),
    ]