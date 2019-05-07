# Generated by Django 2.2.1 on 2019-05-07 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0002_auto_20190507_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=128, verbose_name='诗歌名')),
                ('paragraphs', models.CharField(default='', max_length=128, verbose_name='诗歌名')),
                ('strains', models.CharField(default='', max_length=128, verbose_name='诗歌名')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poem.AuthorModel')),
            ],
            options={
                'verbose_name': '诗歌',
                'verbose_name_plural': '诗歌',
            },
        ),
    ]
