from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .models import SeriesModel, SeasonModel
import os


class SeriesView(View):

    template = os.path.join('series', 'series.html')

    series = SeriesModel.objects.all()
    seasons = SeasonModel.objects.all()

    context = {
        'all_seasons': seasons,
        'all_series': series
    }

    def get(self, request):
        return render(request, self.template, self.context)

    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def post(self, request):
        return HttpResponseRedirect('/series')
