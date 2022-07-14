from src.streamnai.libraries import *
from src.streamnai.utils import process_audio

#initalize the class 
process_audio_obj = process_audio()

audio_file_path = 'sample_audio.mp3'

#RETURNS Status code and transcript
'''
starts the transcribe job and gets the transcript.
parameters:
    audio_file_path: the path to the audio file to be transcribed.
    is_medical: boolean value indicating if the audio file is medical or not.
    vocabulary_name: the vocabulary name to be used for the transcribe job.
    LanguageModelName: the language model name to be used for the transcribe job.
returns:
    transcript: the transcript of the audio file.
        
'''
print( process_audio_obj.transcribe_audio( audio_file_path = audio_file_path , is_medical = True , vocabulary_name = '' , LanguageModelName = '') )