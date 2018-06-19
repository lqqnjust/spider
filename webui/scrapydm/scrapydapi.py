# coding:utf-8
import time

import requests

from django.conf import settings

try:
    SERVER_URL = settings.SCRAPYD_URL
except:
    SERVER_URL = "http://localhost:6800"

def addversion( project_name,version, file_path):
    with open(file_path, 'rb') as f:
        eggdata = f.read()
    response = requests.post(SERVER_URL + '/addversion.json', data={
        'project': project_name,
        'version': version,
        'egg': eggdata,
    })
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok':
            return data['spiders']
    return None

def addvesiondata(project_name, file):
    eggdata = file.read()
    response = requests.post(SERVER_URL + '/addversion.json', data={
        'project': project_name,
        'version': int(time.time()),
        'egg': eggdata,
    })
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok':
            return data['spiders']
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
    if resp.status_code == 200:
        data = resp.json()
        print(data)
        if data['status'] == 'ok':
            return data['spiders']
        else:
            return 0
    return None


def listjobs(project_name):
    resp = requests.get(SERVER_URL + "/listjobs.json?project=%s" % project_name)
    if resp.status_code == 200:
        data = resp.json() 
        if data['status'] == 'ok':
            return (data['pending'], data['running'], data['finished'])
        else:
            return None
    return None

def main():
    # addversion('doubanspider','douban.egg')
    # print(listspiders('doubanspider'))
    # print(schedule('doubanspider','doubangroup',{}))
    # print(listjobs('doubanspider'))
    # print(cancel('doubanspider','2f8188f669f011e887f7509a4c3a4459'))
    print(listprojects())

if __name__ == '__main__':
    main()