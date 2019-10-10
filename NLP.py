from google.cloud import texttospeech
from google.cloud import exceptions




###############################################################################
# Developer: Abdullah Najjar
# Description: Read 3 books from text files provided from an open source project, 
# then, allows Google API to read through the text using natural language processing.
# Books: The stranger by Albert Camus, 
# Bugs: 0, Needs testing to find out which parts are missing, add 2 books and sources
# Date: 10 October, 2019
###############################################################################
def readBook():
#input file #1 for The stranger
input_file_1 = open("TheStranger-AlbertCamus.txt","r")
book_1 = input_file_1.read()
input_file_1.close()

#input file #2 for 
input_file_2 = open("TheStranger-AlbertCamus.txt","r")
book_2 = input_file_2.read()
input_file_2.close()

#input file #3 for
input_file_3 = open("TheStranger-AlbertCamus.txt","r")
book_3 = input_file_3.read()
input_file_3.close()

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
  
  
