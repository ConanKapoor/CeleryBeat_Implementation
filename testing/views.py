# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import os, subprocess, sys

# Create your views here.
def url_retrieval(request):
    if request.method == 'POST':
        web_url = request.POST.get('user')

        b = subprocess.check_output("nslookup %s" %web_url, shell = True)
        f = open('ouput_of_request', 'w')
        f.write(b)
        f.close()
    return render(request, 'testing/userdata.html')
