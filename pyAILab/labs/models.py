# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

######################################
# Lab
######################################


# A laboratory
class Lab(models.Model):

    # Fields
    name = models.CharField(max_length=100, verbose_name=u"Name")
    description = models.TextField(null=False, verbose_name=u"Description")
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u"Creation date")

# end Lab
