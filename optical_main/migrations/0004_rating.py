# Generated by Django 4.2.4 on 2024-12-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optical_main', '0003_alter_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200)),
            ],
        ),
    ]
