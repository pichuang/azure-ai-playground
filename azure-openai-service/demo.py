#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script demonstrates how to use the Azure OpenAI Service to generate a chat completion.
It requires the `openai` package and environment variables for configuration.
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

endpoint = os.getenv("AOAI_ENDPOINT")
model_name = os.getenv("AOAI_MODEL_NAME")
deployment = os.getenv("AOAI_DEPLOYMENT_NAME")
subscription_key = os.getenv("AOAI_KEY")
api_version = os.getenv("AOAI_API_VERSION", "2024-12-01-preview")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_completion_tokens=800,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    model=deployment
)

print(response.choices[0].message.content)
