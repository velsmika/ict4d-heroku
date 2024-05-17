from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import models
from .forms import UploadFileForm
from .formhandler import handle_uploaded_file_menu, handle_uploaded_file_farmer
from django.shortcuts import render
from ict4ddb.models import MenuAudio, FarmerAudioNL, FarmerAudioEN

from datetime import datetime

#upload file audio's
def upload_file_menu(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if(request.POST["audio_type"] == "menu"):
                handle_uploaded_file_menu(form.cleaned_data['file'].file.read(), request.POST["lang"], request.POST["audio_name"])
    else:
        form = UploadFileForm()
        return render(request, "upload.html", {"form": form})

def upload_file_farmer(request):
    if request.method == "POST":
        if request.POST["lang"] == "nl":
            fa = FarmerAudioNL()
            fa.audio = request.FILES["file"].read()
            fa.audio_name = "fa-" + datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            fa.language = request.POST["lang"]
            fa.seedtype = request.POST["seedtype"]
            fa.amount = request.POST["amount"]
            fa.save()
        elif request.POST["lang"] == "en":
            fa = FarmerAudioEN()
            fa.audio = request.FILES["file"].read()
            fa.audio_name = "fa-" + datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            fa.language = request.POST["lang"]
            fa.seedtype = request.POST["seedtype"]
            fa.amount = request.POST["amount"]
            fa.save()

#get file audio's for the menu    
def get_menu_audio(request, lang, name):
    if request.method == "GET":
         menuAudio = MenuAudio.objects.get(language=lang, audio_name=name)
         response = HttpResponse(menuAudio.audio, content_type='audio/mpeg')
         response['Content-Length'] = len(menuAudio.audio)
         return response
		
#get number of items in farmeraudio for lang
def get_amount_farmer_audio_seedtype(request, lang):
    if request.method == "GET":
        if lang == 'nl':
            jr = {"amount":FarmerAudioNL.objects.filter(language=lang).count()}
            return JsonResponse(jr)
        elif lang == 'en':
            jr = {"amount":FarmerAudioEN.objects.filter(language=lang).count()}
            return JsonResponse(jr)
    
def get_farmer_audio(request, lang, id):
    if request.method == "GET":
        if lang == "nl":
            fa = FarmerAudioNL.objects.get(id=id)
            return HttpResponse(fa.audio, content_type='audio/mpeg')
        elif lang == "en":
            fa = FarmerAudioEN.objects.get(id=id)
            return HttpResponse(fa.audio, content_type='audio/mpeg')
					