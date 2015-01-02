#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.shortcuts import Http404
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from os import popen
from django.http import HttpResponse
from django.utils.translation import gettext as _


def test(request):
    return render_to_response('test.html', {'language': _('language')})
