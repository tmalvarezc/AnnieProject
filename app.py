import sounddevice as sd
from scipy.io.wavfile import write
from google.cloud import storage
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import soundfile as sf
from google.cloud import language


def upload_to_gcloud(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
#write('output.wav', fs, myrecording)  # Save as WAV file
sf.write('myfile.flac', myrecording, fs)

upload_to_gcloud('voice-bucket-01','myfile.flac','myfile.flac')

client = speech_v1.SpeechClient()

encoding = enums.RecognitionConfig.AudioEncoding.FLAC
sample_rate_hertz = 44100
language_code = 'en-US'
config = {'encoding': encoding, 'sample_rate_hertz': sample_rate_hertz, 'language_code': language_code}
uri = 'gs://voice-bucket-01/myfile.flac'
audio = {'uri': uri}

response = client.recognize(config, audio)
print(response)

# parsing
#response
#text to speech
# dialflow
