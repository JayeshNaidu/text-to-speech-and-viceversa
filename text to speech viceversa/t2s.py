from gtts import gTTS
import os
import speech_recognition as sr




def t2s():
	txt = input('\nEnter text:\n')
	lang = 'en'
	obj = gTTS(text = txt,lang = lang,slow=False)
	obj.save('sample.mp3')
	os.system('sample.mp3')




def s2t():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('speak something')
		aud = r.listen(source)
		try:
			text = r.recognize_google(aud,language='eng-in')
			print('you said: ',text)
		except:
			print('Sorry try again')





if __name__ == '__main__':
	c = int(input('Choose mode\n1.Text 2 Speech\n2.Speech to Text'))
	if(c==1):
		t2s()
	elif(c==2):
		s2t()
	else:
		print('invalid input')

