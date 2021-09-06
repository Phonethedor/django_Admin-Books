# Generated by Django 3.2.7 on 2021-09-06 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(db_column='client_id', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('joined_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'clients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(db_column='billing_id', primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('charged_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'billing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(db_column='leads_id', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('registered_datetime', models.DateTimeField()),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'leads',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(db_column='site_id', primary_key=True, serialize=False)),
                ('domain_name', models.CharField(max_length=100)),
                ('created_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'sites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'libro',
            },
        ),
        migrations.CreateModel(
            name='Publicador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('libros', models.ManyToManyField(related_name='publicador', to='polls.Libro')),
            ],
            options={
                'db_table': 'publicador',
            },
        ),
    ]
