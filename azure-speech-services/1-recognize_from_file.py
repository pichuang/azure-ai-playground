#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script demonstrates how to use the Azure Cognitive Services Speech SDK to recognize speech from the default microphone.
"""
import os
import time
import azure.cognitiveservices.speech as speechsdk
import dotenv

dotenv.load_dotenv()

SPEECH_KEY = os.getenv('SPEECH_KEY')
ENDPOINT = os.getenv('ENDPOINT')
TLS_VALIDATION_ENABLED = os.getenv('TLS_VALIDATION_ENABLED', 'true')
PROXY_HOST = os.getenv('PROXY_HOST')
PROXY_PORT = int(os.getenv('PROXY_PORT'))
TEST_WAV_FILE = os.getenv('TEST_WAV_FILE', 'test.wav')

def recognize_from_file():
    """
    Recognizes speech from a specified WAV file and prints the recognized text.
    """
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        endpoint=ENDPOINT)
    speech_config.speech_recognition_language="en-US"

    # PropertyId Enum
    # https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech.propertyid?view=azure-python

    speech_config.set_property_by_name("OPENSSL_CONTINUE_ON_CRL_DOWNLOAD_FAILURE", "true")
    speech_config.set_property_by_name("OPENSSL_DISABLE_CRL_CHECK", "true")

    audio_config = speechsdk.AudioConfig(filename=TEST_WAV_FILE)

    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config)

    done = False
    all_results = []

    def recognized_cb(evt):
        print(f"RECOGNIZED: {evt.result.text}")
        all_results.append(evt.result.text)

    def stop_cb(evt):
        print(f"STOPPED: {evt}")
        nonlocal done
        done = True

    def canceled_cb(evt):
        print(f"CANCELED: {evt}")
        nonlocal done
        done = True

    speech_recognizer.recognized.connect(recognized_cb)
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(canceled_cb)

    speech_recognizer.start_continuous_recognition_async()

    while not done:
        time.sleep(0.5)

    speech_recognizer.stop_continuous_recognition_async()

    print("\nFull Transcript:")
    print(" ".join(all_results))

recognize_from_file()
