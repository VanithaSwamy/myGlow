# Generated by Django 4.1.7 on 2023-04-16 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('palour', '0012_parlour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parlour',
            name='username',
        ),
        migrations.AlterField(
            model_name='parlour',
            name='parlour_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palour.clientdetail'),
        ),
    ]
