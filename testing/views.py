# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import os, subprocess, sys
from tasks import nslookup, nmap

web_url = "www.cyware.com"
# Create your views here.
def url_retrieval(request):
    # if request.method == 'POST':
    #     web_url = request.POST.get('user')

    return render(request, 'testing/userdata.html')
