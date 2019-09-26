from google.cloud import texttospeech
from google.cloud import exceptions





#Read book function stuff - need editions->
#Add the book to be read, then add two others if possible and install reqs. and test 
def readBook():
#book = "TheStranger-AlbertCamus"

#Instance of a client
client = texttospeech.TextToSpeechClient()

#Set the text input to be synthesized
synthesis_in = texttospeech.types.SynthesisInput(text="welcome")

#voice request
voice = texttospeech.types.VoiceSelectionParams(language_code='en-US', ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

#type of audio file to be returned 
audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)

#response
response = client.synthesize_speech(synthesis_input, voice, audio_config)

#response content, and output file
with open('Annie_output', 'wb') as out:
  out.write(response.audio_content)
  print('Audio output in file "Annie_output.mp3"')
