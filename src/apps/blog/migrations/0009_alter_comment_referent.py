# Generated by Django 4.0.4 on 2022-04-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_referent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='referent',
            field=models.IntegerField(blank=True, null=True, verbose_name='Референт'),
        ),
    ]
