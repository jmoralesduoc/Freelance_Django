# Generated by Django 5.0.6 on 2024-07-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfreelance', '0002_oferta'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]