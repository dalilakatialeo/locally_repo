# Generated by Django 3.2.5 on 2021-09-11 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='donation',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
                ('amount', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
                ('donor', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='projects.project')),
            ],
        ),
    ]