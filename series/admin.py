from django.contrib import admin
from .models import SeriesModel, AddedSeriesModel, SeasonModel, EpisodeModel

admin.site.register(SeriesModel)
admin.site.register(AddedSeriesModel)
admin.site.register(SeasonModel)
admin.site.register(EpisodeModel)