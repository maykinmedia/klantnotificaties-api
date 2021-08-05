# Generated by Django 2.2.24 on 2021-08-05 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zgw_consumers', '0012_auto_20210104_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactmomenten_service', models.OneToOneField(help_text='Contactmomenten API in which CONTACTMOMENTen will be created when a KlantNotificatie is created.', limit_choices_to={'api_type': 'cmc'}, null=True, on_delete=django.db.models.deletion.PROTECT, to='zgw_consumers.Service', verbose_name='Contactmomenten API')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
