#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The python script ONLY works on Azure VM with User Assigned Managed Identity.

You CANNNOT run this script on your local machine, because local machine does not have User Assigned Managed Identity.
"""


import os
import dotenv
from azure.identity import ManagedIdentityCredential
from azure.cognitiveservices.speech import SpeechConfig
from use_jwt_to_access import recognize_from_file_with_jwt


dotenv.load_dotenv()

# https://learn.microsoft.com/zh-tw/azure/ai-services/speech-service/how-to-configure-azure-ad-auth?tabs=portal&pivots=programming-language-python#create-a-custom-domain-name
CUSTOM_ENDPOINT = os.getenv("CUSTOM_ENDPOINT")
USER_ASSIGNED_CLIENT_ID = os.getenv("USER_ASSIGNED_CLIENT_ID")

# Please make sure you assign the User Assigned Managed Identity to the Azure Cognitive Services resource.
credential = ManagedIdentityCredential(client_id=USER_ASSIGNED_CLIENT_ID)
credential.get_token("https://cognitiveservices.azure.com/.default")

token = credential.get_token("https://cognitiveservices.azure.com/.default")
jwt_token = token.token

speechConfig = SpeechConfig(token_credential=credential, endpoint=CUSTOM_ENDPOINT)

print(f"取得的 JWT token: {jwt_token}")

recognize_from_file_with_jwt(jwt_token, "test.wav")
