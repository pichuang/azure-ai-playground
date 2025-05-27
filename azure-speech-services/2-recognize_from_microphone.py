#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script demonstrates how to use the Azure Cognitive Services Speech SDK to recognize speech from the default microphone.
"""
import os
import azure.cognitiveservices.speech as speechsdk
import dotenv

dotenv.load_dotenv()

SPEECH_KEY = os.getenv('SPEECH_KEY')
ENDPOINT = os.getenv('ENDPOINT')
TLS_VALIDATION_ENABLED = os.getenv('TLS_VALIDATION_ENABLED', 'true')
PROXY_HOST = os.getenv('PROXY_HOST')
PROXY_PORT = int(os.getenv('PROXY_PORT'))
TEST_WAV_FILE = os.getenv('TEST_WAV_FILE', 'test.wav')

def recognize_from_microphone():
    """
    Recognizes speech from the default microphone and prints the recognized text.
    """

    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        endpoint=ENDPOINT)
    speech_config.speech_recognition_language="en-US"

    # Enable Proxy if specified
    # Note!! Proxy functionality is not available on macOS. This function will have no effect on the platform
    speech_config.set_proxy(hostname=PROXY_HOST, port=PROXY_PORT, username=None, password=None)
    speech_config.enable_audio_logging()

    # PropertyId Enum
    # https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech.propertyid?view=azure-python

    speech_config.set_property_by_name("OPENSSL_CONTINUE_ON_CRL_DOWNLOAD_FAILURE", "true")
    speech_config.set_property_by_name("OPENSSL_DISABLE_CRL_CHECK", "true")

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and endpoint values?")

recognize_from_microphone()

