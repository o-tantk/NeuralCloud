# Generated by Django 4.1.4 on 2023-01-08 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algorithm', '0008_alter_stat_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='algorithm',
            options={'ordering': ['name_kr']},
        ),
        migrations.CreateModel(
            name='Useless',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_kr', models.CharField(blank=True, max_length=30)),
                ('algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='algorithm.algorithm')),
                ('stats', models.ManyToManyField(related_name='+', to='algorithm.stat')),
            ],
        ),
    ]