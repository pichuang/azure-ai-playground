#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import dotenv
from azure.identity import ManagedIdentityCredential
from azure.cognitiveservices.speech import SpeechConfig
from use_jwt_to_access import recognize_from_file_with_jwt


dotenv.load_dotenv()

# https://learn.microsoft.com/zh-tw/azure/ai-services/speech-service/how-to-configure-azure-ad-auth?tabs=portal&pivots=programming-language-python#create-a-custom-domain-name
CUSTOM_ENDPOINT = os.getenv("CUSTOM_ENDPOINT")
USER_ASSIGNED_CLIENT_ID = os.getenv("USER_ASSIGNED_CLIENT_ID")

credential = ManagedIdentityCredential(client_id=USER_ASSIGNED_CLIENT_ID)
token = credential.get_token("https://cognitiveservices.azure.com/.default")
jwt_token = token.token

speechConfig = SpeechConfig(token_credential=credential, endpoint=CUSTOM_ENDPOINT)

print(f"取得的 JWT token: {jwt_token}")

recognize_from_file_with_jwt(jwt_token, "test.wav")
