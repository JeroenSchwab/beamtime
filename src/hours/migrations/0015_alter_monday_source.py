# Generated by Django 3.2.3 on 2021-07-10 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0014_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monday',
            name='Source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hours.source'),
        ),
    ]
