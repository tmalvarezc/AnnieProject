from google.cloud import texttospeech
#from google.cloud import exceptions


print("Hello")

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
    input_file_first = open("TheStranger-AlbertCamus.txt","r")
    book_first = input_file_first.read()
    input_file_first.close()
    #input file #2 for
    input_file_sec = open("TheStranger-AlbertCamus.txt","r")
    book_sec = input_file_sec.read()
    input_file_sec.close()
    #input file #3 for
    input_file_third = open("TheStranger-AlbertCamus.txt","r")
    book_third = input_file_third.read()
    input_file_third.close()
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
    #response content, and output files
    with open('Annie_output', 'wb') as out:
        out.write(response.audio_content)
        print('Audio output in file "Annie_output.mp3"')
