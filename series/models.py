from django.db import models
from user.models import ProfileModel


class SeriesModel(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField()
    image_path = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Series'
        verbose_name_plural = 'Series'
        ordering = ('-date_added',)


class AddedSeriesModel(models.Model):

    series = models.ForeignKey(SeriesModel, on_delete=models.CASCADE, related_name='added_series')
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='added_series')
    date_started = models.DateTimeField(auto_now_add=True)
    date_finished = models.DateTimeField(null=True)
    is_finished = models.BooleanField(default=False)
    current_season = models.IntegerField()
    current_episode = models.IntegerField()
    personal_rating = models.IntegerField()

    def __str__(self):
        return "Added Series: " + self.series.name

    class Meta:

        verbose_name = 'Added Series'
        verbose_name_plural = 'Added Series'
        ordering = ('-date_started',)


class SeasonModel(models.Model):

    series = models.ForeignKey(SeriesModel, on_delete=models.CASCADE, related_name='seasons')
    order = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Season: " + str(self.order)

    class Meta:

        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'
        ordering = ('-date_added',)


class EpisodeModel(models.Model):

    season = models.ForeignKey(SeasonModel, on_delete=models.CASCADE, related_name='episodes')
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Episode: " + self.name

    class Meta:

        verbose_name = 'Episode'
        verbose_name_plural = 'Episodes'
        ordering = ('-date_added',)
