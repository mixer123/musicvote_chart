from datetime import datetime
import datetime
from django.db import models
SCORES = (
    (0, "0"),

)
# Create your models here.
class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    vote = models.SmallIntegerField(choices=SCORES, default=0)
    vote_prev = models.SmallIntegerField(default=0)
    place = models.SmallIntegerField(default=0)
    status = models.TextField(max_length=20, default='Nowość')
    data_list = models.DateTimeField(default=datetime.datetime.today())
    list_per_page = 2

    def __str__(self):
        return self.title
class IP(models.Model):
        ip = models.TextField(default='', max_length=15)
        song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

        # def __str__(self):
        #     return self.ip