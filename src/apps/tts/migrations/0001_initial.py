# Generated by Django 2.2.1 on 2019-05-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TTSProviderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, verbose_name='供应商名字')),
                ('api_url', models.CharField(default='', max_length=512, verbose_name='请求URL')),
                ('app_id', models.CharField(default='', max_length=128, verbose_name='应用ID')),
                ('app_key', models.CharField(default='', max_length=512, verbose_name='应用Key')),
            ],
            options={
                'verbose_name_plural': '语音合成提供商',
                'verbose_name': '语音合成提供商',
            },
        ),
    ]
