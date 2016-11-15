from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
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
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
else:
    with open('env.json') as data_file:
        data = json.load(data_file)
        CLIENT_ID = data["CLIENT_ID"]
        TMDB_API_KEY = data['TMDB_API_KEY']

def hello_world(request):
    
    # return HttpResponse("Hello World")
    return render(request, 'index.html')

class HelloWorld(TemplateView):
    template_name = 'index.html'

class SearchView(APIView):
    def get(self, request, show, format=None):
        query = show
        query.replace(" ", "%20")
        headers = {
        'Content-Type': 'application/json',
        # 'X-Pagination-Page': request.META.get('X-Pagination-Page') or 1,
        # 'X-Pagination-Limit': request.META.get('X-Pagination-Limit') or 10,
        'trakt-api-version': '2',
        'trakt-api-key': CLIENT_ID
        }
        re = requests.get('https://api.trakt.tv/search/show?query=' + query + "&limit=20", headers=headers)

        print(re)
        return HttpResponse(re, content_type="application/json")

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
# LoginRequiredMixin
class DetailList(APIView):
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

class SearchViewV2(APIView):
    def get(self, request, show, format=None):
        query = show
        query.replace(" ", "%20")
        re = requests.get('http://api.tvmaze.com/search/shows?q=' + query)
        
        return HttpResponse(re, content_type="application/json")

class SingleSearchV2(APIView):
    def get(self, request, show, format=None):
        query = show
        query.replace(" ", "%20")
        re = requests.get('http://api.tvmaze.com/singlesearch/shows?q=' + query)
        
        return HttpResponse(re, content_type="application/json")

class IDSearchV2(APIView):
    def get(self, request, id, format=None):
        query = id
        re = requests.get('http://api.tvmaze.com/shows/{}'.format(query))
        return HttpResponse(re, content_type="application/json")

class ShowEpisodes(APIView):
    def get(self, request, id, format=None):
        query = id
        re = requests.get('http://api.tvmaze.com/shows/{}/episodes'.format(query))
        
        return HttpResponse(re, content_type="application/json")

class TrendingView(APIView):
    def get(self, request, format=None):
        headers = {
        'Content-Type': 'application/json',
        'trakt-api-version': '2',
        'trakt-api-key': CLIENT_ID
        }
        request1 = requests.get('https://api.trakt.tv/shows/trending?extended=full', headers=headers)
        request1 = request1.json()
        test2 = []
        for show in request1:
            # print(show['show']['ids'])
            request2 = requests.get('http://api.tvmaze.com/lookup/shows?imdb={}'.format(show['show']['ids']['imdb']))
            test2.append(request2.json())
        
        # response_body = urlopen(request).read()
        # print(response_body)
        return JsonResponse(test2, safe=False)

class PopularView(APIView):
    def get(self, request, format=None):

        popular = requests.get('https://api.themoviedb.org/3/tv/popular?api_key={}&language=en-US'.format(TMDB_API_KEY))
        # response_body = urlopen(request).read()
        # print(response_body)
        popular = popular.json()

        for show in popular['results']:
            show['poster_img'] = 'https://image.tmdb.org/t/p/w500/{}'.format(show['poster_path'])

        return JsonResponse(popular, safe=False)

class TestView(APIView):
    def get(self, request, format=None):
        d = {
            'name': 'name',
            'date': 'date',
            'amount': 'amount'
        }
        if d.keys() != ['amount', 'name']:
            raise ValueError("DSDS")

        return HttpResponse("Hi")

