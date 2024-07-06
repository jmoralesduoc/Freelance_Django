# Generated by Django 5.0.6 on 2024-07-05 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfreelance', '0003_usuario_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]