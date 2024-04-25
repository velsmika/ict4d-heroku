from django.db import models

class MenuAudio(models.Model):
	language = models.CharField(max_length=2)
	audio_name = models.TextField()
	audio = models.BinaryField()

class FarmerAudio(models.Model):
	language = models.CharField(max_length=2)
	audio_name = models.TextField()
	audio = models.BinaryField()