from ict4ddb.models import MenuAudio

def handle_uploaded_file_menu(f, lang, file_name):
	handle_uploaded_file(f, lang, file_name, 'menu')
	
def handle_uploaded_file_farmer(f, lang, file_name):
	handle_uploaded_file(f, lang, file_name, 'farmer')

def handle_uploaded_file(f, lang, file_name, model):
	binaryFileData = ''
	for chunk in f.chunks :
		binaryFileData += chunk
	if(model == 'menu'):
		ma = MenuAudio()
		ma.language = lang
		ma.audio_name = file_name
		ma.audio = binaryFileData
		ma.save()
	# elif(model == 'farmer'):
	# 	fa = FarmerAudio()
	# 	fa.language = lang
	# 	fa.audio_name = file_name
	# 	fa.audio = binaryFileData
	# 	fa.save()