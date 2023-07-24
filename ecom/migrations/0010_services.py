# Generated by Django 3.0.5 on 2023-07-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0009_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('service_image', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]