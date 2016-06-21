# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
'''
Initial django functions

@author: Laurent GAY
@organization: sd-libre.fr
@contact: info@sd-libre.fr
@copyright: 2015 sd-libre.fr
@license: This file is part of Lucterios.

Lucterios is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lucterios is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Lucterios.  If not, see <http://www.gnu.org/licenses/>.
'''

from __future__ import unicode_literals

from django.db import migrations
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from lucterios.CORE.models import Parameter


def addon_create_account(apps, schema_editor):
    translation.activate(settings.LANGUAGE_CODE)
    param = Parameter.objects.create(name='contacts-createaccount', typeparam=4)
    param.title = _("contacts-createaccount")
    param.param_titles = (_("contacts-createaccount.0"),
                          _("contacts-createaccount.1"), _("contacts-createaccount.2"))
    param.args = "{'Enum':3}"
    param.value = '0'
    param.save()


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_addon'),
    ]

    operations = [
        migrations.RunPython(addon_create_account),
    ]
