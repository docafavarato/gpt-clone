import openai
from datetime import datetime
import urllib.request
from flask import escape
import os

openai.api_key = "YOUR_API_KEY"
def ask(question, temperature):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=temperature,
)

    message = str(escape(completions['choices'][0]['text'])).replace("\n", "<br/>")
    return message

def create_image(prompt):
    image_resp = openai.Image.create(prompt=prompt, n=4, size="512x512")
    for image in image_resp['data']:
        url = image['url']
        filename = f"{str(datetime.now()).replace(' ', '').replace('.', '').replace(':', '')}nameofimage{prompt}.jpg"
        folder = 'static/generated_images'
        full_path = os.path.join(folder, filename)
        urllib.request.urlretrieve(url, full_path)
    return image_resp

def retrieve_images():
    images = dict()
    for image in os.listdir('static/generated_images'):
        try:
            images[image] = [image, image.split('nameofimage')[1].split('.jpg')[0]]
        except:
            pass
        
    return images

