# This code is generated based on the following specification using GitHub Copilot (powered by GPT-4):
# 
# Specification:
# Implement a Python app that describes an image in detail using Langchain and Ollama with the model Gemma3:4b.
#
# Requirements:
# - The app should take the image located at ./asset/sample.png.
# - Display the image (sample.png) in the default web browser.
# - Use the Gemma3:4b model to describe the image in detail.
# - Print the description in the terminal.

import os
import webbrowser
from pathlib import Path
import base64

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

# Set the path to the image
current_dir = Path(__file__).parent
image_path = current_dir / "asset" / "sample.png"

# Ensure the image exists
if not image_path.exists():
    raise FileNotFoundError(f"Image not found at {image_path}")

# Open the image in the default web browser
print(f"Opening image in browser: {image_path}")
webbrowser.open(f"file://{image_path.absolute()}")

# Read the image file as bytes and encode as base64
with open(image_path, "rb") as image_file:
    image_data = image_file.read()
    base64_image = base64.b64encode(image_data).decode('utf-8')

# Create the ChatOllama instance with the gemma3:4b model
llm = ChatOllama(
    model="gemma3:4b",
    temperature=0.1,
)

# Create a prompt with the base64-encoded image
message = HumanMessage(
    content=[
        {
            "type": "text", 
            "text": "Please describe this image in detail. What do you see in it?"
        },
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}"
            }
        }
    ]
)

# Get the image description from the model
print("Generating image description...")
response = llm.invoke([message])

# Print the description
print("\nImage Description:")
print("-----------------")
print(response.content)
