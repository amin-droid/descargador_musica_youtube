from django.shortcuts import render
from moviepy.editor import VideoFileClip
from .forms import VideoLink
import os
import urllib.request
# Create your views here.
from pytube import YouTube
# from selenium import webdriver
# from selenium.webdriver.common.by import By
def index(request):
    if request.method=='POST':
        print(request)
    return render(request,'index.html')
    

def searchbar(request):
    resolutions = []
    SAVE_PATH = "f:/" #to_do 
    if request.method == 'POST':
        search = request.POST['search']
        yt = YouTube(search)
        # t=yt.streams.get_highest_resolution()
        t = yt.thumbnail_url
        #t[0].download()
        # t.download(SAVE_PATH)
        # video = VideoFileClip(os.path.join(t.default_filename,"to","movie.mp4"))
        # # video.audio.write_audiofile(os.path.join(t.title,"to","movie_sound.mp3"))
        # video.audio.write_audiofile
        print(t)
        for stream in yt.streams.all():
            print(type(stream.resolution))
            if stream.resolution != None:

                resolutions.append(stream.resolution)
        context ={
            'search':yt,
            'resolutions':resolutions
       }
    return render(request,'index.html',context)