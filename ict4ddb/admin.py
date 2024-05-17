from django.contrib import admin
from .models import MenuAudio, FarmerAudioDutch, FarmerAudioEnglish, FAD, FAE

admin.site.register(MenuAudio)
admin.site.register(FarmerAudioEnglish)
admin.site.register(FarmerAudioDutch)
admin.site.register(FAD)
admin.site.register(FAE)
