# Generated by Django 3.2.16 on 2023-11-28 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0006_usercommentrelations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercommentrelations',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_app.comment'),
        ),
    ]