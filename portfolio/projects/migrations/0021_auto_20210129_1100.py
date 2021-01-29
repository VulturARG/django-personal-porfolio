# Generated by Django 2.2 on 2021-01-29 14:00

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_auto_20210129_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Summary'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Description'),
        ),
    ]