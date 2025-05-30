# Generated by Django 5.2.1 on 2025-05-23 12:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=500, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Полный текст записи'),
        ),
    ]
