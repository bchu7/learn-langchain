
# first pull the model by run command: ollama pull bakllava

import webbrowser
import base64
from io import BytesIO

from IPython.display import HTML, display
from PIL import Image

from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

from langchain_core.output_parsers import StrOutputParser

def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="PNG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def plt_img_base64(img_base64):
    """
    Disply base64 encoded string as image

    :param img_base64:  Base64 string
    """
    # Create an HTML img tag with the base64 string as the source
    image_html = f'<img src="data:image/jpeg;base64,{img_base64}" />'
    # Display the image by rendering the HTML
    # display(HTML(image_html))

    image_html = f'<html><body><img src="data:image/jpeg;base64,{img_base64}" /></body></html>'
    with open("temp_image.html", "w") as f:
        f.write(image_html)
    webbrowser.open("temp_image.html")


file_path = "./asset/sample.png"
pil_image = Image.open(file_path)

image_b64 = convert_to_base64(pil_image)

# display image
plt_img_base64(image_b64)

# llm = ChatOllama(model="bakllava", temperature=0)
llm = ChatOllama(model="gemma3:4b", temperature=0)

def prompt_func(data):
    text = data["text"]
    image = data["image"]

    image_part = {
        "type": "image_url",
        "image_url": f"data:image/jpeg;base64,{image}",
    }

    content_parts = []

    text_part = {"type": "text", "text": text}
    # system_part = {"type": "system", "text": system}

    content_parts.append(image_part)
    content_parts.append(text_part)
    # content_parts.append(system_part)

    return [HumanMessage(content=content_parts)]


chain = prompt_func | llm | StrOutputParser()
query_chain = chain.invoke(
    {
     "text": "Please describe in detail what you see in the image",
     "context:": "You are a helpfull assistant, please answer user question politely",
     "image": image_b64
    }
)

print(query_chain)