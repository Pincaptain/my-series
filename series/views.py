from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .models import SeriesModel, SeasonModel, AddedSeriesModel
from user.models import ProfileModel
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


class AddSeries(View):

    def get(self, request):
        pass

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        series = SeriesModel.objects.get(id=request.POST['id'])
        profile = ProfileModel.objects.get(user=request.user)

        added = AddedSeriesModel.objects.create(series=series, profile=profile)
        added.save()

        return HttpResponseRedirect('/user')