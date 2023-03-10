# Generated by Django 4.1.4 on 2022-12-30 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AlgorithmBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('name_kr', models.CharField(max_length=30)),
                ('slot', models.CharField(choices=[('OFF', 'Offense'), ('STB', 'Stability'), ('SPC', 'Special')], default='OFF', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Doll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('name_kr', models.CharField(max_length=30)),
                ('doll_class', models.CharField(choices=[('GRD', 'Guard'), ('WRR', 'Warrior'), ('SNI', 'Sniper'), ('MED', 'Medic'), ('SPC', 'Specialist')], default='GRD', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_kr', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_kr', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Combination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algorithm.doll')),
                ('offense', models.ForeignKey(limit_choices_to={'base__slot': 'OFF'}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='algorithm.algorithm')),
                ('special', models.ForeignKey(limit_choices_to={'base__slot': 'SPC'}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='algorithm.algorithm')),
                ('stability', models.ForeignKey(limit_choices_to={'base__slot': 'STB'}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='algorithm.algorithm')),
            ],
        ),
        migrations.AddField(
            model_name='algorithm',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='algorithm.algorithmbase'),
        ),
        migrations.AddField(
            model_name='algorithm',
            name='primary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='algorithm.primarystat'),
        ),
        migrations.AddField(
            model_name='algorithm',
            name='secondary0',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='algorithm.secondarystat'),
        ),
        migrations.AddField(
            model_name='algorithm',
            name='secondary1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='algorithm.secondarystat'),
        ),
    ]
