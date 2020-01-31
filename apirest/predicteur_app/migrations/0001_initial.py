# Generated by Django 3.0.2 on 2020-01-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reassignment_count', models.FloatField()),
                ('reopen_count', models.FloatField()),
                ('sys_mod_count', models.FloatField()),
                ('made_sla', models.FloatField()),
                ('u_priority_confirmation', models.FloatField()),
                ('knowledge', models.FloatField()),
                ('Duree_openToClose', models.FloatField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]