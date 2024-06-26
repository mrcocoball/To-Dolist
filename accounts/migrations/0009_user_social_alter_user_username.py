# Generated by Django 4.1.7 on 2023-03-27 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='social',
            field=models.BooleanField(default=False, null=True, verbose_name='SOCIAL'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': '이미 존재하는 닉네임입니다.'}, max_length=15, unique=True),
        ),
    ]
