from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from .forms import UploadFileForm
from .formhandler import handle_uploaded_file_menu, handle_uploaded_file_farmer
from django.shortcuts import render
from ict4ddb.models import MenuAudio


def upload_file_menu(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if(type == "menu"):
                handle_uploaded_file_menu(request.FILES["file"])
            else:
                 handle_uploaded_file_farmer(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "templates/ict4d/upload.html", {"form": form})
    
def get_menu_audio(request, lang, name):
	if request.method == "GET":
		menuAudio = MenuAudio.objects.filter(language=lang, audio_name=name).values()
		return HttpResponse(menuAudio.audio, headers={'"Content-Type"="audio/mpeg"'})
					