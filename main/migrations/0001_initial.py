# Generated by Django 4.0 on 2022-05-07 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_category_image_alter_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(upload_to='Banner/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннер',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.CharField(max_length=250, verbose_name='Что нового')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
