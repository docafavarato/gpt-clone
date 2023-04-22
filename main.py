from flask import Flask, render_template, request, url_for
from models import ask, create_image


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    if request.method == 'POST':
        question = request.form.get('question')
        answer = ask(question)
        return render_template('index.html', answer=answer)
    
@app.route('/images')
def index_images():
    return render_template('images.html')

@app.route('/images', methods=['POST'])
def images_post():
    if request.method == 'POST':
        description = request.form.get('description')
        images = create_image(description)['data']
        return render_template('images.html', images=images)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
