# Generated by Django 3.2.13 on 2022-06-18 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cusid', models.IntegerField(primary_key=True, serialize=False)),
                ('cusname', models.CharField(max_length=30)),
                ('mobnum', models.CharField(max_length=10)),
                ('emailid', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('seatnum', models.IntegerField()),
                ('bookdate', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.customer')),
            ],
        ),
    ]