# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

######################################
# Lab
######################################


# A laboratory
class Lab(models.Model):
    """
    A laboratory
    """

    # Fields
    name = models.CharField(max_length=100, null=False, verbose_name=u"Name")
    slug = models.CharField(max_length=100, null=False, verbose_name=u"Slug")
    description = models.TextField(null=False, verbose_name=u"Description")
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u"Creation date")

    ##################################
    # Override
    ##################################

    # To string
    def __str__(self):
        """
        Transform model to string
        :return:
        """
        return "Lab({})".format(self.name)
    # end __str__

    # To Unicode
    def __unicode__(self):
        """
        Transform model to unicode
        :return:
        """
        return u"Lab({})".format(self.name)
    # end __unicode__

# end Lab


######################################
# Experience
######################################


# An experience
class Experience(models.Model):
    """
    An experience
    """

    # Fields
    name = models.CharField(max_length=100, null=False, verbose_name=u"Name")
    slug = models.CharField(max_length=100, null=False, verbose_name=u"Slug")
    description = models.TextField(null=False, verbose_name=u"Description")
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u"Creation date")
    open = models.BooleanField(default=True, null=False, verbose_name=u"Open")
    lab = models.ForeignKey('Lab', null=False, verbose_name=u"Lab")

    ##################################
    # Override
    ##################################

    # To string
    def __str__(self):
        """
        Transform model to string
        :return:
        """
        return "Experience({})".format(self.name)
    # end __str__

    # To Unicode
    def __unicode__(self):
        """
        Transform model to unicode
        :return:
        """
        return u"Experience({})".format(self.name)
    # end __unicode__

# end Experience
