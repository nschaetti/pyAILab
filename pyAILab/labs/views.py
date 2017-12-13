# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from labs.models import Lab, Experience


#####################################
# HOME
#####################################

# Homepage with lab list
def home(request):
    """
    Home page with lab list,
    show all the labs
    :param request:
    :return:
    """
    # Get all labs
    labs = Lab.objects.all()

    # Render template
    return render(request, 'labs/home.html', {'labs': labs})
# end home

#####################################
# VIEW LAB MAIN
#####################################


# View a lab main page
def view_lab_main(request, slug):
    """
    View a lab's main page
    :param request:
    :return:
    """
    # Try to get the lab
    lab = get_object_or_404(Lab, slug=slug)

    # Get all experiences
    xps = Experience.objects.filter(lab_id=lab.id)

    # Render template
    return render(request, 'labs/lab.html', {'lab': lab, 'xps': xps})
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
    # Try to get the experience
    lab = get_object_or_404(Lab, slug=lab_slug)
    xp = get_object_or_404(Experience, slug=xp_slug, lab=lab.id)

    # Render template
    return render(request, 'labs/xp.html', {'xp': xp})
# end view_xp_main
