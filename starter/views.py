from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import Request, urlopen
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

import json
import os
import requests

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

class HelloWorld(TemplateView):
    template_name = 'index.html'

def search(request):
    query = request.GET.get('show', 'game-of-thrones')
    headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': CLIENT_ID
    }
    request = Request('https://api.trakt.tv/search/show?query=' + query, headers=headers)

    response_body = urlopen(request).read()
    print(response_body)
    return HttpResponse(response_body)

def details(request):
    query = request.GET.get('show', 'game-of-thrones')
    headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': CLIENT_ID
    }
    request = Request('https://api.trakt.tv/shows/' + query, headers=headers)

    response_body = urlopen(request).read()
    print(response_body)
    return HttpResponse(response_body)

class DetailList(LoginRequiredMixin, APIView):
    def get(self, request, show, format=None):
        query = show
        headers = {
        'Content-Type': 'application/json',
        'trakt-api-version': '2',
        'trakt-api-key': CLIENT_ID
        }
        request = requests.get('https://api.trakt.tv/shows/' + query + "?extended=full", headers=headers)

        # response_body = urlopen(request).read()
        # print(response_body)
        return Response(request.json())

def test(request, page_num):
    return HttpResponse(page_num)