import openai

openai.api_key = "YOUR_API_KEY"
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
    return image_resp
