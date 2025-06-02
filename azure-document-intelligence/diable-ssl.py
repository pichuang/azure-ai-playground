#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ssl
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
import numpy as np

# 全域關閉 SSL 驗證（在非正式環境才這麼做）
ssl._create_default_https_context = ssl._create_unverified_context

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
ENDPOINT = "https://di-jpe.cognitiveservices.azure.com/"
KEY = ""
FORM_URL = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"

def format_bounding_box(bounding_box):
    """
    Format the bounding box coordinates into a string representation.
    """
    if not bounding_box:
        return "N/A"
    reshaped_bounding_box = np.array(bounding_box).reshape(-1, 2)
    return ", ".join([f"[{x}, {y}]" for x, y in reshaped_bounding_box])

def analyze_read():
    """
    This sample demonstrates how to use the Document Intelligence client library to analyze a document using the prebuilt Read model.
    It retrieves the text content, bounding boxes, and confidence scores for each word in the document.
    """


    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=ENDPOINT,
        credential=AzureKeyCredential(KEY),
    )

    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-read",
        AnalyzeDocumentRequest(url_source=FORM_URL)
    )
    result = poller.result()

    print ("Document contains content: ", result.content)

    for style in enumerate(result.styles):
        print(
            f"Document contains {'handwritten' if style.is_handwritten else 'no handwritten'} content"
        )

    for page in result.pages:
        print(f"----Analyzing Read from page #{page.page_number}----")
        print(
            f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}"
        )

        for line_idx, line in enumerate(page.lines):
            print(
                f"...Line # {line_idx} has text content '{line.content}' within bounding box '{format_bounding_box(line.polygon)}'"
            )

        for word in page.words:
            print(
                f"...Word '{word.content}' has a confidence of {word.confidence}"
            )

    print("----------------------------------------")


if __name__ == "__main__":
    analyze_read()
