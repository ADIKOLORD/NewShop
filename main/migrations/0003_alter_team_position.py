# Generated by Django 4.0 on 2022-05-09 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(choices=[('DIRECTOR', 'DIRECTOR'), ('DIRECTOR', 'MENEDJER'), ('WEB DEVELOPER', 'WEB DEVELOPER'), ('DESING', 'DESING'), ('BACK END DEVELOPER', 'BACK END DEVELOPER')], default='3', max_length=50),
        ),
    ]