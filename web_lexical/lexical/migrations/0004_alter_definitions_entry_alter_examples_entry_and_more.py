# Generated by Django 4.1.6 on 2023-02-24 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lexical', '0003_alter_entries_lexicalcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definitions',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexical.entries', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='examples',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lexical.entries', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='synonyms',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lexical.entries', verbose_name='Category'),
        ),
    ]