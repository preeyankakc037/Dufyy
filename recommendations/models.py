from django.db import models

class Song(models.Model):
    music_name = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    music_link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["music_name"]

    def __str__(self):
        return f"{self.music_name} - {self.artist_name}"
