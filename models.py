import openai
from datetime import datetime
import urllib.request
import os

openai.api_key = "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"
def ask(question):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
)

    message = completions['choices'][0]['text']
    return message

def create_image(prompt):
    image_resp = openai.Image.create(prompt=prompt, n=4, size="512x512")
    for image in image_resp['data']:
        url = image['url']
        filename = f"{str(datetime.now()).replace(' ', '').replace('.', '').replace(':', '')}name{prompt}.jpg"
        folder = 'static/generated_images'
        full_path = os.path.join(folder, filename)
        urllib.request.urlretrieve(url, full_path)
    return image_resp

def retrieve_images():
    images = dict()
    for image in os.listdir('static/generated_images'):
        try:
            images[image] = [image, image.split('name')[1].split('.jpg')[0]]
        except:
            pass
        
    return images

print(retrieve_images())