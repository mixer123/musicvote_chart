# Create your views here.
import matplotlib
from django.contrib.sites import requests
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

from django.core.paginator import Paginator
from . models import Song
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from django.http import HttpResponse
from matplotlib import pylab
from pylab import *
import base64
from io import BytesIO
import PIL, PIL.Image
from io import StringIO

from .plots import bar_plot

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')

    return render(request, 'ip.html', {'ip': ip})





def songs(request):
    msg=" czas nie minął"
    date_now = datetime.datetime.today()
    list_ip = []
    for i in IP.objects.all():
        list_ip.append(i.ip)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        address_ip = x_forwarded_for.split(',')[-1].strip()
    else:
        address_ip = request.META.get('REMOTE_ADDR')
    status_ip = False

    if address_ip in list_ip:
        status_ip = True



    songs = Song.objects.all().order_by('-vote')
    i=1
    for song in songs:

        date1 = date_now.minute
        print(date1)

        date2 = song.data_list.minute
        print(date1)
        print(date2)
        print('diff',date1-date2)


        if (date1 - date2) > 45:
            msg='czas minął'
            song.vote_prev = song.vote
            # song.vote = 0
            song.save()
        Song.objects.filter(id=song.id).update(place=i)
        i+=1
    songs = Song.objects.all().order_by('place')
    paginator = Paginator(songs, 3)
    page_number = request.GET.get('page')
    page_songs = paginator.get_page(page_number)

    return render(request,"songs.html",{'songs':songs,"page_songs":page_songs, 'status_ip':status_ip,'msg':msg})


def song_detail(request, id):



    song = get_object_or_404(Song, id=id)




    list_ip =[]
    for i in IP.objects.all():
        list_ip.append(i.ip)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        address_ip = x_forwarded_for.split(',')[-1].strip()
    else:
        address_ip = request.META.get('REMOTE_ADDR')

    vote = song.vote

    status_ip = False
    # pass the object as instance in form
    if address_ip in list_ip:
        status_ip = True
        print(status_ip)
        form = SongForm()
        ip_instance = IP.objects.get(ip=address_ip)
        print(ip_instance.song_id.title)
        # return render(request, 'song_detail.html', {'song_detail': song,'form':form})
        return render(request, 'message_ip.html', {'song_detail': ip_instance.song_id.title, 'status_ip':status_ip})
    else:
        if request.method == 'POST':
            form = SongForm(request.POST)

            if form.is_valid() :
                vote1 = form.cleaned_data['vote']
                ip_instance = IP(ip=address_ip, song_id=song)
                ip_instance.save()
                song.vote += 1
                song.status = " W górę"
                song.save()

                vote_next = song.vote

                # if vote_next - vote_prev > 0:
                #    status = " W górę"

                return render(request, 'message.html')
        else:
            form = SongForm(initial={'vote': 1})
            # form_ip = IPForm()


    return render(request, 'song_detail.html', {'song_detail': song, 'form':form, 'status_ip':status_ip})





def ranking(request):
    vote_count = Song.objects.all().order_by('-vote')
    sales_df = pd.DataFrame(vote_count.values())
    title = sales_df['title'].to_numpy()
    votes = sales_df['vote'].to_numpy()
    graph = bar_plot(title, votes, votes)
    # plt.show()
    return render(request, 'ranking.html', {'vote_count': vote_count, 'image':graph})

#
