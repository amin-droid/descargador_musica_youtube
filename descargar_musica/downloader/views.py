from django.shortcuts import render
from moviepy.editor import VideoFileClip
from .forms import VideoLink
import os
# Create your views here.
from pytube import YouTube
# from selenium import webdriver
# from selenium.webdriver.common.by import By
def index(request):
    if request.method=='POST':
        print(request)
    return render(request,'index.html')
    

def searchbar(request):
    if request.method == 'POST':
        search = request.POST['search']
        yt = YouTube(search)
        t=yt.streams.filter(progressive=True, file_extension='mp4').first()
        #t[0].download()
        t.download()
        video = VideoFileClip(os.path.join(t.default_filename,"to","movie.mp4"))
        video.audio.write_audiofile(os.path.join(t.title,"to","movie_sound.mp3"))
        video.audio.write_audiofile
    return render(request,'index.html')