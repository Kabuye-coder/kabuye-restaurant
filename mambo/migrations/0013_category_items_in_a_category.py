# Generated by Django 4.2.5 on 2023-11-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mambo', '0012_remove_category_items_in_a_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='items_in_a_category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
