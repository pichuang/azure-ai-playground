#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import dotenv
from openai import AzureOpenAI

dotenv.load_dotenv()

client = AzureOpenAI(
    azure_endpoint = os.getenv("AZURE_AI_FOUNDRY_PROJECT_ENDPOINT"),
    api_key=os.getenv("AZURE_AI_FOUNDRY_PROJECT_KEY"),
    api_version="2024-05-01-preview",
)

# Create an assistant
assistant = client.beta.assistants.create(
    model=os.getenv("DEPLOYMENT_NAME"),
    name="Data Visualization",
    instructions="You are a helpful AI assistant who makes interesting visualizations based on data."
    "You have access to a sandboxed environment for writing and testing code."
    "When you are asked to create a visualization you should follow these steps:"
    "1. Write the code."
    "2. Anytime you write new code display a preview of the code to show your work."
    "3. Run the code to confirm that it runs."
    "4. If the code is successful display the visualization."
    "5. If the code is unsuccessful display the error message and try to revise the code and rerun going through the steps from above again.",
    tools=[{"type": "code_interpreter"}],
)
