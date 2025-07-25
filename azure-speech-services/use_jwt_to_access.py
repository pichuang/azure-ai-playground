#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import dotenv
import azure.cognitiveservices.speech as speechsdk

dotenv.load_dotenv()
SPEECH_REGION = os.getenv("SPEECH_REGION")
CUSTOM_ENDPOINT = os.getenv("CUSTOM_ENDPOINT")

def recognize_from_file_with_jwt(jwt_token, audio_file: str):
    """
    Uses a JWT token to authenticate with Azure Cognitive Services Speech SDK
    """

    # https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech.speechconfig?view=azure-python#parameters
    if CUSTOM_ENDPOINT:
        # pylint: disable=pointless-string-statement
        """
        If CUSTOM_ENDPOINT is set, use it to create the SpeechConfig.
        Due to some technical limitations, you need to assign the JWT token to the SpeechServiceAuthorization_Token property after creating the SpeechConfig with the custom endpoint.
        """
        print(f"Using custom endpoint: {CUSTOM_ENDPOINT}")
        speech_config = speechsdk.SpeechConfig(endpoint=CUSTOM_ENDPOINT)
        # https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech.propertyid?view=azure-python
        speech_config.set_property(speechsdk.PropertyId.SpeechServiceAuthorization_Token, jwt_token)
    else:
        if not SPEECH_REGION:
            raise ValueError("SPEECH_REGION is not set. " \
                            "Please set it in your environment variables.")

        print(f"Using region: {SPEECH_REGION}")
        speech_config = speechsdk.SpeechConfig(region=SPEECH_REGION, auth_token=jwt_token)

    speech_config.speech_recognition_language = "en-US"
    audio_config = speechsdk.AudioConfig(filename=audio_file)
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    done = False
    all_results = []

    def recognized_cb(evt):
        print(f"RECOGNIZED: {evt.result.text}")
        all_results.append(evt.result.text)

    def stop_cb(evt):
        nonlocal done
        done = True

    def canceled_cb(evt):
        details = evt.result.cancellation_details
        print(f"CANCELED reason={details.reason}, error={details.error_details}")
        nonlocal done
        done = True

    speech_recognizer.recognized.connect(recognized_cb)
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(canceled_cb)

    speech_recognizer.start_continuous_recognition_async()

    while not done:
        time.sleep(0.5)

    speech_recognizer.stop_continuous_recognition_async()
    print("\n完整結果:")
    print(" ".join(all_results))

if __name__ == "__main__":
    EXAMPLE_JWT_TOKEN = "<YOUR_JWT_TOKEN>"
    AUDIO_FILE_PATH = "test.wav"
    recognize_from_file_with_jwt(EXAMPLE_JWT_TOKEN, AUDIO_FILE_PATH)