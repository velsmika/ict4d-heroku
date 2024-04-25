from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from .forms import UploadFileForm
from ict4d.models import MenuAudio, FarmerAudio
from .formhandler import handle_uploaded_file_menu, handle_uploaded_file_farmer
from django.shortcuts import render


def upload_file_menu(request, lang, name, type):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if(type == "menu"):
                handle_uploaded_file_menu(request.FILES["file"], lang, name)
            else:
                 handle_uploaded_file_farmer(request.FILES["file"], lang, name)
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})
    
def get_menu_audio(request, lang, name):
	if request.method == "GET":
		menuAudio = MenuAudio.objects.filter(language=lang, audio_name=name).values()
		return HttpResponse(menuAudio.audio, headers={'"Content-Type"="audio/mpeg"'})
					