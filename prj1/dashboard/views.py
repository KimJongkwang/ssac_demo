from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse

from .repository import NationRepository
import json


# Create your views here.

class HomeView(TemplateView):
    template_name = 'dashboard/home.html'

class SearchView(View):
    def get(self, request, key):
        repository = NationRepository()
        searched_nation = repository.select_nation_by_name(key)
        json_nation = json.dumps(searched_nation, ensure_ascii=False, cls=DjangoJSONEncoder)
        return HttpResponse(json_nation, content_type="application/json")

class StationView(View):
    def get(self, request, key):
        repository = NationRepository()
        searched_nation = repository.select_station_by_nation(key)
        json_nation = json.dumps(searched_nation, ensure_ascii=False, cls=DjangoJSONEncoder)
        return HttpResponse(json_nation, content_type="application/json")

class AirDetail(View):
    def get(self, request, key):
        repository = NationRepository()
        clicked_staion = repository.show_data_by_station(key)
        # ["nation", "obs_dt", "stn_nm", "no2", "o3", "co2", "so2", "pm10", "pm25"]
        # clicked_staion 
        # year = 
        json_station = json.dumps(clicked_staion, ensure_ascii=False, cls=DjangoJSONEncoder)
        return HttpResponse(json_station, content_type="application/json")