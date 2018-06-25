from django.urls import path
from .views import SeriesView, AddSeries, ChangeSeries, FinishSeries

urlpatterns = [
    path('', SeriesView .as_view(), name='series'),
    path('add/', AddSeries.as_view(), name='add'),
    path('change/', ChangeSeries.as_view(), name='change'),
    path('finish/', FinishSeries.as_view(), name='finish'),
]