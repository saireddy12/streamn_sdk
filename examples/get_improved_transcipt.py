from src.streamnai.libraries import *
from src.streamnai.utils import process_audio

#initalize the class 
process_audio_obj = process_audio()

audio_file_path = 'sample_audio.mp3'

#RETURNS Status code and transcript

'''
starts the audio lab job and does iteration to get improved transcript.
parameters:
    audio_file_path: the path to the audio file to be transcribed.
    is_medical: boolean value indicating if the audio file is medical or not.
    media_file_extension: the extension of the media file.
returns:
    transcript: the improved transcript of the audio file.
        
'''

#transcibe an audio file and return improved transcript
print( process_audio_obj.get_improved_transcript( audio_file_path = audio_file_path , is_medical = True , vocabulary_name = '' , LanguageModelName = '' ) )


