# Generated by Django 4.1.4 on 2022-12-30 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algorithm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm',
            name='secondary0',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='algorithm.secondarystat'),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='secondary1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='algorithm.secondarystat'),
        ),
    ]
