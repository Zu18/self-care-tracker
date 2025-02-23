# Generated by Django 5.1.5 on 2025-01-30 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfcare', '0002_dailyactivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField()),
                ('entry_text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selfcare.user')),
            ],
            options={
                'db_table': 'journal',
            },
        ),
        migrations.CreateModel(
            name='PersonalGoals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_title', models.CharField(max_length=100)),
                ('goal_description', models.TextField()),
                ('target_date', models.DateField()),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selfcare.user')),
            ],
            options={
                'db_table': 'personal_goals',
            },
        ),
    ]
