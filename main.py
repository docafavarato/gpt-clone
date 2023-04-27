from flask import Flask, render_template, request, url_for
from models import ask, create_image, retrieve_images

app = Flask(__name__)
app.jinja_env.autoescape = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    if request.method == 'POST':
        match request.form['options']:
            case "exato":
                temperature = 0.3
            case "padrao":
                temperature = 0.5
            case "criativo":
                temperature = 0.8
        question = request.form.get('question')
        answer = ask(question, temperature)
        return render_template('answer.html', answer=answer) # 0.3: exato / 0.5: padrão / 0.8: criativo
    
@app.route('/images')
def index_images():
    return render_template('images.html')

@app.route('/images', methods=['POST'])
def images_post():
    if request.method == 'POST':
        description = request.form.get('description')
        images = create_image(description)['data']
        return render_template('image_answer.html', images=images)
    
@app.route('/gallery')
def gallery_images():
    images = retrieve_images()
    return render_template('gallery.html', images=images)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)