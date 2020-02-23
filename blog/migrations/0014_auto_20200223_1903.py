# Generated by Django 3.0.3 on 2020-02-23 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200221_1913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created_on'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
