# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


#####################################
# HOME
#####################################

# Homepage with lab list
def home(request):
    """
    Home page with lab list
    :param request:
    :return:
    """
    return render(request, 'labs/home.html')
# end home

#####################################
# VIEW LAB MAIN
#####################################


# View a lab main page
def view_lab_main(request, lab_slug):
    """
    View a lab's main page
    :param request:
    :return:
    """
    return render(request, 'labs/lab.html', {'lab_slug': lab_slug})
# end view_lab_main

#####################################
# VIEW LAB MAIN
#####################################


# View an xp main page
def view_xp_main(request, lab_slug, xp_slug):
    """
    View an xp main page
    :param request:
    :param lab_slug:
    :param xp_slug:
    :return:
    """
    return render(request, 'labs/xp.html', {'lab_slug': lab_slug, 'xp_slug': xp_slug})
# end view_xp_main
