# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ast_model', '0003_auto_20150311_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astnode',
            name='name',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='astnode',
            name='type_str',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
