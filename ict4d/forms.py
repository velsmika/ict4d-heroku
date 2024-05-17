from django import forms

class UploadFileForm(forms.Form):
    audio_type = forms.CharField(max_length=10)
    audio_name= forms.CharField(max_length=50)
    lang = forms.CharField(max_length=2)
    file = forms.FileField()

class UploadFarmerAudioForm(forms.Form):
    audio_name= forms.CharField(max_length=20)
    lang = forms.CharField(max_length=2)
    file = forms.FileField()
    amount = forms.IntegerField()
    seedtype = forms.CharField(max_length=20)