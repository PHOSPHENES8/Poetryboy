# Generated by Django 2.2.1 on 2019-05-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0005_auto_20190507_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='poemmodel',
            name='audio',
            field=models.FileField(null=True, upload_to='', verbose_name='诗歌朗读文件'),
        ),
    ]