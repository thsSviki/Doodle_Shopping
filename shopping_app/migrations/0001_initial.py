# Generated by Django 2.2.11 on 2020-03-21 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image', models.ImageField(default='img/index.jpeg', upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='User_log',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('rates', models.FloatField()),
                ('nam', models.CharField(max_length=200)),
                ('purchaser', models.ForeignKey(blank=True, default='foobar', on_delete=django.db.models.deletion.CASCADE, to='shopping_app.User_log')),
            ],
        ),
    ]
