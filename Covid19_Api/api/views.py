from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import urllib
import json
import requests

@api_view(['GET'])
def All_wilaya_stats(request):
    if request.method == 'GET':
        response = requests.get(
            "https://api.apify.com/v2/key-value-stores/pp4Wo2slUJ78ZnaAi/records/LATEST?disableRedirect=true")

        data = json.loads(response.text)
        wilaya_list = []
        for region in data["infectedByRegion"]:
            to_json = {
                'Wilaya': region["region"],
                'cases': region["value"]
            }
            wilaya_list.append(to_json)
        dump = json.dumps(wilaya_list)
        return Response(json.loads(dump) ,status=status.HTTP_200_OK)


@api_view(['GET'])
def Wilaya_stats(request ,pkt):
    response = requests.get(
        "https://api.apify.com/v2/key-value-stores/pp4Wo2slUJ78ZnaAi/records/LATEST?disableRedirect=true")

    data = json.loads(response.text)
    wilaya = dict()
    for region in data["infectedByRegion"] :
          if region["region"] == pkt:
               wilaya = {
                 'Wilaya': region["region"],
                  'cases': region["value"]
              }
    dump = json.dumps(wilaya)
    return Response(json.loads(dump) ,status=status.HTTP_200_OK)

@api_view(["GET"])
def live_stats(request):
    response = requests.get("https://api.thevirustracker.com/free-api?countryTotal=DZ")
    data = json.loads(response.text)
    stats = {
        'total_cases': data['countrydata'][0]['total_cases'],
        'total_recovered': data['countrydata'][0]['total_recovered'],
        'total_deaths': data['countrydata'][0]['total_deaths'],
        'total_new_cases_today': data['countrydata'][0]['total_new_cases_today'],
        'total_new_deaths_today': data['countrydata'][0]['total_new_deaths_today'],
        'total_serious_cases': data['countrydata'][0]['total_serious_cases']}

    dump = json.dumps(stats)
    return Response(json.loads(dump) ,status=status.HTTP_200_OK)

@api_view(["GET"])
def time_line(request):
    response = requests.get("https://api.thevirustracker.com/free-api?countryTimeline=DZ")
    data = json.loads(response.text)
    dump = json.dumps(data['timelineitems'])
    return Response(json.loads(dump), status=status.HTTP_200_OK)