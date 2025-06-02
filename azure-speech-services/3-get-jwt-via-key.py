#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import requests
import dotenv
from use_jwt_to_access import recognize_from_file_with_jwt

# Load environment variables from .env file
dotenv.load_dotenv()

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")

TOKEN_ENDPOINT = f"https://{SPEECH_REGION}.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

headers = {
    "Ocp-Apim-Subscription-Key": SPEECH_KEY,
    "Content-Length": "0"
}

response = requests.post(
    TOKEN_ENDPOINT,
    headers=headers,
    data="",
    timeout=10)
jwt_token = response.text.strip()

print(f"取得的 JWT token: {jwt_token}")

recognize_from_file_with_jwt(jwt_token, "test.wav")
