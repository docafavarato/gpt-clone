import openai
from datetime import datetime
import urllib.request
import json
import os

openai.api_key = ""
def ask(question, temperature):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=temperature,
    )
    message = str(completions['choices'][0]['text']).replace("\n", "<br/>")
    match message[:10]:
        case "<br/><br/>":
            better = message[10:].lstrip()
        case _:
            better = message
    return better

def create_image(prompt):
    image_resp = openai.Image.create(prompt=prompt, n=4, size="512x512")
    for image in image_resp['data']:
        with open('static/generated_images/images.json', 'r+') as file:
            data = json.load(file)
            data["images"][image["url"]] = prompt
        with open('static/generated_images/images.json', 'w') as file:
            json.dump(data, file)

    return image_resp

def retrieve_images():
    images = dict()
    with open('static/generated_images/images.json', 'r') as file:
        data = json.load(file)
        for image in data["images"]:
            try:
                images[image] = data["images"][image]
            except:
                pass
        
    return images
