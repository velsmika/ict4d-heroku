from ict4ddb.models import MenuAudio

def handle_uploaded_file_menu(f, lang, file_name):
	handle_uploaded_file(f, lang, file_name, 'menu')
	
def handle_uploaded_file_farmer(f, lang, file_name):
	handle_uploaded_file(f, lang, file_name, 'farmer')

def handle_uploaded_file(f, lang, file_name, model):
	if(model == 'menu'):
		ma = MenuAudio()
		ma.language = lang
		ma.audio_name = file_name
		ma.audio = f.read()
		ma.save()
	# elif(model == 'farmer'):
	# 	fa = FarmerAudio()
	# 	fa.language = lang
	# 	fa.audio_name = file_name
	# 	fa.audio = binaryFileData
	# 	fa.save()