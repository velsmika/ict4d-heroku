from django import forms

class UploadFileForm(forms.Form):
    audio_name= forms.CharField(max_length=50)
    file = forms.FileField()