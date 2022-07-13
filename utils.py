from libraries import *
from config import *
import time


def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        logging.info("{}".format(msg))
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry



class hit_api:

    def __init__( self ):
        pass


    def create_new_transcribe_job( self, job_id , audio_file_path , is_medical , vocabulary_name = '',LanguageModelName=''):
        '''
        This function creates a new transcribe job and returns the job id.
        parameters:
            job_id: the job id to be used for the transcribe job.
            audio_file_path: the path to the audio file to be transcribed.
            is_medical: boolean value indicating if the audio file is medical or not.
        returns:
            job_id: the job id of the transcribe job.
        '''

        #audio_file_name = os.path.basename(audio_file_path)
        url = CREATE_AWS_TRANSCRIPT_URL

        headers = {
            'accept': 'application/json',
            'Authorization':API_KEY,
            # requests won't add a boundary if this header is set when you pass files=
            # 'Content-Type': 'multipart/form-data',
            }
        
        params = {
            'jobid': job_id,
            'is_medical':is_medical,
            'SPECIALITY':'PRIMARYCARE',
            'Type':'DICTATION',
            'vocabulary_name':vocabulary_name,
            'LanguageModelName':LanguageModelName,
        }

        files = {
            'upload_file': open( audio_file_path , 'rb' ),
        }

        response = requests.post( url , params = params , headers = headers , files = files )

        return response.status , response.text


    #create_new_transcribe_job( job_id = JOB_ID , audio_file_path = SAMPLE_AUDIO_FILE_PATH , is_medical = True )


    def get_aws_transcript( self , job_id , is_medical ):
        '''
        This function gets the aws transcript of the audio file.
        parameters:
            job_id: the job id of the transcribe job.
            is_medical: boolean value indicating if the audio file is medical or not.
        returns:
            aws_transcript: the aws transcript of the audio file.
        '''

        url = GET_AWS_TRANSCRIPT_URL

        params = {
            'jobid': job_id ,
            'is_medical': is_medical ,
            }
        
        headers = {
            'Authorization': API_KEY,
        }

        response = requests.post( url , params = params , headers = headers )
        
        return response.status , json.loads(response.text)


    def start_audio_lab_job( self , job_id ):
        '''
        This function starts the audio lab job and returns the results.
        parameters:
            job_id: the job id of the transcribe job.
        returns:
            results: the results of the transcribe job.
        '''

        url = START_AUDIO_LAB_URL

        params = {
            'job_id': job_id 
            }

        headers = {
            'Authorization':API_KEY,
        }

        response = requests.post( url , params = params , headers = headers )

        return response.status , json.loads(response.text)

    
    def get_audio_lab_results(self , job_id ):
        '''
        This function gets the audio lab results and returns the results.
        parameters:
            job_id: the job id of the transcribe job.
        returns:
            results: transcript with audio lab results
        '''
        
        url = GET_AUDIO_LAB_TRANSCRIPT

        headers = {
            'Authorization': API_KEY
            }
        
        params = {
            'job_id': job_id
        }

        response = requests.post( url , params = params , headers = headers )

        return response.status , json.loads(response.text)


    
    def start_and_get_improved_transcript_results( self , job_id , is_medical , media_file_extension = '.mp3' ):
        '''
        This function starts the gets the improved transcript and returns the results.
        parameters:
            job_id: the job id of the transcribe job.
            is_medical: boolean value indicating if the audio file is medical or not.
            media_file_extension: the extension of the media file.
        returns:
            results: improved transcribe of the job.
        
        '''

        url = GET_IMPROVED_TRANSCRIPT_URL

        params = {
            'job_id': job_id ,
            'is_medical': is_medical ,
            'media_file_extension': media_file_extension ,
        }

        headers = {
            'Authorization': API_KEY ,
        }

        response = requests.post( url , params = params , headers = headers )

        return response.status , json.loads(response.text)

    
    

    
class process_audio(hit_api):

    def __init__(self):
        self.job_id = None

    def get_transcript( self , audio_file_path , is_medical ):
        '''
        starts the transcribe job and gets the transcript.
        parameters:
            audio_file_path: the path to the audio file to be transcribed.
            is_medical: boolean value indicating if the audio file is medical or not.
        returns:
            transcript: the transcript of the audio file.
        
        '''
        #if audio file is not present return error
        if not os.path.isfile( audio_file_path ):
            return 'Error: Audio file not found'
        
        job_id = audio_file_path.split('/')[-1].split('.')[0] 
        response_status_code , job_id = self.create_new_transcribe_job( job_id = job_id , audio_file_path = audio_file_path , is_medical = is_medical )
        self.job_id = job_id
        if response_status_code != 200:
            return response_status_code , 'Error: Unable to create transcribe job'
        else:
            #get aws transcript
            response_status_code , transcript = self.get_aws_transcript( job_id = job_id , is_medical = is_medical ) 

            if response_status_code != 200:
                return response_status_code , 'Error: Unable to get aws transcript'
        
        return response_status_code , transcript

    
    def get_audiolab_transcript( self , audio_file_path , is_medical , media_file_extension = '.mp3' ):
        '''
        starts the audio lab job and adds audio lab info
        parameters:
            audio_file_path: the path to the audio file to be transcribed.
            is_medical: boolean value indicating if the audio file is medical or not.
            media_file_extension: the extension of the media file.
        returns:
            transcript: the transcript with audio lab scores added.
        
        '''
        transcipt = ''
        response_status_code , transcipt = self.get_transcript( self , audio_file_path , is_medical )

        if response_status_code!=200:
            return response_status_code , transcipt

        #start the audio lab job
        if self.job_id:
            
            #TO-DO , use the below status , before doing next steps
            audiolab_job_start_status = self.start_audio_lab_job( job_id = self.job_id )

            #wait for 15 seconds
            time.sleep(15)
            #To-DO add retry funtionality

            #get audio lab results
            response_status , transcipt = self.get_audio_lab_results( job_id = self.job_id ) 

            #retry again
            if isinstance( transcipt , str ):
                time.sleep(30)
                response_status , transcipt = self.get_audio_lab_results( job_id = self.job_id )  

            if response_status != 200:
                return response_status , 'Error: Unable to get audio lab results'


        return response_status , transcipt

    
    def get_improved_transcript( self , audio_file_path , is_medical , media_file_extension = '.mp3' ):
        '''
        starts the audio lab job and does iteration to get improved transcript.
        parameters:
            audio_file_path: the path to the audio file to be transcribed.
            is_medical: boolean value indicating if the audio file is medical or not.
            media_file_extension: the extension of the media file.
        returns:
            transcript: the improved transcript of the audio file.
        
        '''
        response_status , transcipt = self.get_audiolab_transcript( audio_file_path = audio_file_path , is_medical = is_medical , media_file_extension = media_file_extension )

        if response_status!=200:
            return response_status , 'Error: Unable to get audio lab transcript'
        
        #start the improved transcript job
        if self.job_id:
            response_status , improved_transcript = self.start_and_get_improved_transcript_results( job_id = self.job_id , is_medical = is_medical , media_file_extension = media_file_extension )

        if response_status != 200:
            return response_status , 'Error: Unable to get improved transcript'
        
        return response_status , improved_transcript

    


