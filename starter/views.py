from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import Request, urlopen
import json
import os

CLIENT_ID = None
if os.environ.get('DJANGO_ENV'):
    CLIENT_ID = os.environ.get('CLIENT_ID')
else:
    with open('env.json') as data_file:    
        data = json.load(data_file)
        CLIENT_ID = data["CLIENT_ID"]

def hello_world(request):
    
    # return HttpResponse("Hello World")
    return render(request, 'index.html')

def search(request):
    query = request.GET.get('show', 'tron')
    headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': CLIENT_ID
    }
    request = Request('https://api.trakt.tv/search/show?query=' + query, headers=headers)

    response_body = urlopen(request).read()
    print(response_body)
    return HttpResponse(response_body)