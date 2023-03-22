# Generated by Django 4.1.7 on 2023-03-22 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(choices=[('SILVER', 'SILVER'), ('GOLD', 'GOLD'), ('PLATINUM', 'PLATINUM'), ('DIAMOND', 'DIAMOND'), ('MASTER', 'MASTER')], default='SILVER', max_length=10, null=True, verbose_name='RANK'),
        ),
    ]