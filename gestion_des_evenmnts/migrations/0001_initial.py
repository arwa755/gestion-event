# Generated by Django 3.2.5 on 2021-08-24 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_des_bn_plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='evenement',
            fields=[
                ('publication_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestion_des_bn_plan.publication')),
                ('lieu', models.CharField(max_length=300, verbose_name='lieu exacte')),
                ('date', models.DateTimeField()),
                ('placesDispo', models.PositiveIntegerField(verbose_name='nbre de pLace disponible')),
            ],
            bases=('gestion_des_bn_plan.publication'),
        ),
    ]
