# Generated by Django 2.2 on 2020-12-29 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20201228_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_path', models.FileField(blank=True, default='default/icons.jpg', null=True, upload_to='icons')),
            ],
        ),
    ]
