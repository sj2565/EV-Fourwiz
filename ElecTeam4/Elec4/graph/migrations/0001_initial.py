# Generated by Django 3.2.7 on 2021-10-21 04:30

from django.db import migrations, models
import graph.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='DESCRIPTION')),
                ('slug', models.SlugField(allow_unicode=True, default='', help_text='one word for title alias.', unique=True, verbose_name='SLUG')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('image', graph.fields.ThumbnailImageField(null=True, upload_to='athumb/%Y/%m', verbose_name='IMAGE')),
            ],
            options={
                'verbose_name': 'data',
                'verbose_name_plural': 'datas',
                'db_table': 'graph_datas',
                'ordering': ('id',),
            },
        ),
    ]