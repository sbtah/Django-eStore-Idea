# Generated by Django 3.2 on 2021-09-13 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('products', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
    ]
