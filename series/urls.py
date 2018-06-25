from django.urls import path
from .views import SeriesView, AddSeries

urlpatterns = [
    path('', SeriesView .as_view(), name='series'),
    path('add/', AddSeries.as_view(), name='add'),
]