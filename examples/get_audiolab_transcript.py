from src.streamnai.libraries import *
from src.streamnai.utils import process_audio

#initalize the class 
process_audio_obj = process_audio()

audio_file_path = 'sample_audio.mp3'

#RETURNS Status code and transcript
'''
starts the audio lab job and adds audio lab info
parameters:
    audio_file_path: the path to the audio file to be transcribed.
    is_medical: boolean value indicating if the audio file is medical or not.
    vocabulary_name: the name of the vocabulary to be used.
    LanguageModelName: the name of the language model to be used.
returns:
    transcript: the transcript with audio lab scores added.
        
'''

#transcibe an audio file and return the transcript with audio lab scores
print( process_audio_obj.get_audiolab_transcript( audio_file_path = audio_file_path , is_medical = True , vocabulary_name = '' , LanguageModelName = '' ) )
