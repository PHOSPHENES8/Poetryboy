# Generated by Django 2.2.1 on 2019-05-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0003_poemmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='poemmodel',
            name='dynasty',
            field=models.CharField(default='', max_length=128, verbose_name='朝代'),
        ),
        migrations.AlterField(
            model_name='poemmodel',
            name='paragraphs',
            field=models.CharField(default='', max_length=128, verbose_name='诗歌正文'),
        ),
        migrations.AlterField(
            model_name='poemmodel',
            name='strains',
            field=models.CharField(default='', max_length=128, verbose_name='唱法'),
        ),
    ]
