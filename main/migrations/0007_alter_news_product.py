# Generated by Django 4.0.4 on 2022-05-13 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_count'),
        ('main', '0006_alter_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
