# Image Description Bot

This code is generated based on the following prompt using GitHub Copilot (powered by GPT-4):

```
Specification:
I want to implement a Python app that describes an image in detail using Langchain and Ollama with the model Gemma3:4b.

Requirements:
The app should take the image located at ./asset/sample.png.

When the app is run, it must:
- Display the image (sample.png) in the default web browser.
- Use the Gemma3:4b model to describe the image in detail.
- Print the description in the terminal.

The implementation should fit within a single file, named multi-modal-gen.py.
```

## Prerequisites

1. Install Ollama:
   - Visit [ollama.com](https://ollama.com) and follow the installation instructions for your platform

2. Pull the Gemma 3 4B model:
   ```bash
   ollama pull gemma3:4b
   ```

3. Install the required Python packages:
   ```bash
   pip install langchain-ollama langchain-core pillow
   ```

4. Make sure you have an image file at `./asset/sample.png` relative to the script location

## Running the Application

Execute the application with the following command:

```bash
python multi-modal-gen.py
```

## What the Application Does

When you run the application:
1. It opens the sample.png image in your default web browser
2. Uses the Gemma 3 4B model to generate a detailed description of the image
3. Prints the generated description to the terminal

## Notes

- The first run may take longer as the model is loaded into memory
- Ensure your Ollama service is running before executing the script
- The Gemma 3 4B model must support image understanding capabilities
