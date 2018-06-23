from django.urls import path
from .views import SeriesView

urlpatterns = [
    path('', SeriesView .as_view(), name='series')
]