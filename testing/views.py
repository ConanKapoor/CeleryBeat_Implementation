# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import os, subprocess, sys
from tasks import nslookup, nmap

# Create your views here.
def url_retrieval(request):
    if request.method == 'POST':
        web_url = request.POST.get('user')

        nslookup.delay(web_url)
        nmap.delay(web_url)
    return render(request, 'testing/userdata.html')
