# coding:utf-8
import time

import requests

from django.conf import settings

try:
    SERVER_URL = settings.SCRAPYD_URL
except:
    SERVER_URL = "http://localhost:6800"

def addversion( project_name, file_path):
    with open(file_path, 'rb') as f:
        eggdata = f.read()
    response = requests.post(SERVER_URL + '/addversion.json', data={
        'project': project_name,
        'version': int(time.time()),
        'egg': eggdata,
    })
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok':
            return data['spiders']
        else:
            return data
    return None

def schedule( project_name, spider_name, arguments):
    post_data = dict(project=project_name, spider=spider_name)
    post_data.update(arguments)
    response = requests.post(SERVER_URL + "/schedule.json", data=post_data)
    if response.status_code == 200:
        data = response.json()
        if data['status'] ==  'ok':
            return data['jobid']
    return None

def cancel( project_name, job_id):
    post_data = dict(project=project_name, job=job_id)
    resp = requests.post(SERVER_URL + "/cancel.json", data=post_data, )
    if resp.status_code == 200:
        data = resp.json()
        if data['status'] == 'ok':
            return data['prevstate']
    return None

def listprojects():
    resp = requests.get(SERVER_URL + "/listprojects.json")
    if resp.status_code == 200:
        data = resp.json()
        if data['status'] == 'ok':
            return data['projects']
    return None

def listspiders(project_name):
    resp = requests.get(SERVER_URL + "/listspiders.json?project=%s" % project_name)
    print(resp.status_code)
    if resp.status_code == 200:
        data = resp.json()
        if data['status'] == 'ok':
            return data['spiders']
    return None


def listjobs(project_name):
    resp = requests.get(SERVER_URL + "/listjobs.json?project=%s" % project_name)
    if resp.status_code == 200:
        data = resp.json() 
        if data['status'] == 'ok':
            return (data['pending'], data['running'], data['finished'])
        else:
            return data
    return None

def main():
    ret = addversion("doubanspider",'douban.egg')
    print(ret)

if __name__ == '__main__':
    main()