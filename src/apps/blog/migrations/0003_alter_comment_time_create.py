# Generated by Django 4.0.4 on 2022-04-14 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_options_remove_comment_title_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания комментария'),
        ),
    ]
