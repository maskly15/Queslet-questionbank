# Generated by Django 4.1.7 on 2023-03-06 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionbank', '0005_alter_mcq_table_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcq',
            name='user',
            field=models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AlterModelTable(
            name='mcq',
            table=None,
        ),
    ]
