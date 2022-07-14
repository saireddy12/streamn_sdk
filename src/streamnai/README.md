# More Details on SDK

This SDK offers easy implementation of APIs provided by StreamnAI.

# Key Terms

**What is a job_id?**

>>When you process any audio file through streamn you'll always receive a unique job_id. This jobId is a unique identifier for the job processing the payload you sent.

# Available Methods

streamns APIs provide the functionality for processing audio/Video files and return Transcript


1. transcribe_audio:
    >Parameter Name | Required | Value
    >--- | --- | ---
    >audio_file_path | Mandatory | A valid path to an audio file
    >is_medical | Mandatory | boolean value indicating if the audio file is medical or not.
    >vocabulary_name | optional | the vocabulary name to be used for the transcribe job.
    >LanguageModelName | optional |  the language model name to be used for the transcribe job.
    
    >returns status_code and transcript
    >click [here](https://github.com/saireddy12/streamn_python_sdk/examples/transcribe_audio.py) to check the usage example


2. get_audiolab_transcript:
    >Parameter Name | Required | Value
    >--- | --- | ---
    >audio_file_path | Mandatory | A valid path to an audio file
    >is_medical | Mandatory | boolean value indicating if the audio file is medical or not.
    >vocabulary_name | optional | the vocabulary name to be used for the transcribe job.
    >LanguageModelName | optional |  the language model name to be used for the transcribe job.
    
    >returns status_code and transcript with audio lab score for each word

    >click [here](https://github.com/saireddy12/streamn_python_sdk/examples/get_audiolab_transcript.py) to check the usage example
    

3. get_improved_transcript:
    >Parameter Name | Required | Value
    >--- | --- | ---
    >audio_file_path | Mandatory | A valid path to an audio file
    >is_medical | Mandatory | boolean value indicating if the audio file is medical or not.
    >vocabulary_name | optional | the vocabulary name to be used for the transcribe job.
    >LanguageModelName | optional |  the language model name to be used for the transcribe job.
    
    >returns status_code and transcript with audio lab score for each word

    >click [here](https://github.com/saireddy12/streamn_python_sdk/examples/get_improved_transcipt.py) to check the usage example