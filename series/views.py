from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
import os


class SeriesView(View):

    template = os.path.join('series', 'series.html')
    context = {}

    def get(self, request):
        return render(request, self.template, self.context)

    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def post(self, request):
        return HttpResponseRedirect('/series')
