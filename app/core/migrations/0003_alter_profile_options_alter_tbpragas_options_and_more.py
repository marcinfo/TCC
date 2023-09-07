# Generated by Django 4.2.4 on 2023-09-07 18:57

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tb_registros_tbpragas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Tabela de Perfil', 'verbose_name_plural': 'Tabela de Perfis'},
        ),
        migrations.AlterModelOptions(
            name='tbpragas',
            options={'verbose_name': 'Tabela de Praga', 'verbose_name_plural': 'Tabela de Pragas'},
        ),
        migrations.AlterField(
            model_name='tb_registros',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, help_text='Selecione as imagens da praga.', null=True, upload_to='images', variations={}, verbose_name='Imagem'),
        ),
    ]
