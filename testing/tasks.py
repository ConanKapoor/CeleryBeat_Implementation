from celery import Celery
import os, sys, subprocess

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def nslookup(web_url):
    command_output = subprocess.check_output("nslookup %s" %web_url, shell = True)
    output_file = open('Request_Output_nslookup', 'w')
    output_file.write(command_output)
    output_file.close()

@app.task
def nmap(web_url):
    command_output1 = subprocess.check_output("nmap -v -sS -O %s" %web_url, shell = True)
    output_file1 = open('Request_Output_nmap', 'w')
    output_file1.write(command_output1)
    output_file1.close()
