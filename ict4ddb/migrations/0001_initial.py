# Generated by Django 5.0.4 on 2024-05-16 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerAudioDutch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=2, null=True)),
                ('audio_name', models.CharField(blank=True, max_length=15, null=True)),
                ('audio', models.BinaryField(blank=True, null=True)),
                ('seedtype', models.CharField(blank=True, max_length=20, null=True)),
                ('amount', models.IntegerField()),
                ('phonenumber', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'farmer_audio_dutch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FarmerAudioEnglish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=2, null=True)),
                ('audio_name', models.CharField(blank=True, max_length=15, null=True)),
                ('audio', models.BinaryField(blank=True, null=True)),
                ('seedtype', models.CharField(blank=True, max_length=20, null=True)),
                ('amount', models.IntegerField()),
                ('phonenumber', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'farmer_audio_english',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenuAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=2, null=True)),
                ('audio_name', models.CharField(blank=True, max_length=15, null=True)),
                ('audio', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menu_audio',
                'managed': False,
            },
        ),
    ]