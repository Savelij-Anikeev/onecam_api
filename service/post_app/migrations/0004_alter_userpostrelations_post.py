# Generated by Django 3.2.16 on 2023-11-28 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0003_auto_20231128_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpostrelations',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_app.post'),
        ),
    ]