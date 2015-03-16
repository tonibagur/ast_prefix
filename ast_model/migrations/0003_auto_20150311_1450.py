# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ast_model', '0002_auto_20150310_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='astnode',
            name='col_end',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='astnode',
            name='col_start',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='astnode',
            name='line_end',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='astnode',
            name='line_start',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
