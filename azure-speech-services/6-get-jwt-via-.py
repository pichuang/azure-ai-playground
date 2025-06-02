#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import dotenv
import msal

dotenv.load_dotenv()

TENANT_ID = os.getenv("TENANT_ID", "your-tenant-id")
CLIENT_ID = os.getenv("CLIENT_ID", "your-client-id")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "your-client-secret")

AUTHORITY_URL = f"https://login.microsoftonline.com/{TENANT_ID}"

# 使用 msal函式庫 透過 OIDC WIP 取得 JWT
app = msal.ConfidentialClientApplication(
    client_id=CLIENT_ID,
    authority=AUTHORITY_URL,
    client_credential=CLIENT_SECRET
)

token_result = app.acquire_token_for_client(
    scopes=["https://cognitiveservices.azure.com/.default"]
)

if "access_token" in token_result:
    print(f"取得的 JWT token: {token_result['access_token']}")
else:
    print(f"取得失敗，錯誤資訊: {token_result.get('error_description')}")