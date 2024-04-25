from django import forms

class UploadFileForm(forms.Form):
    audio_type = forms.CharField(max_length=10)
    audio_name= forms.CharField(max_length=50)
    lang = forms.CharField(max_length=2)
    file = forms.FileField()