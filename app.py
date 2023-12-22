from flask import Flask, render_template, request
from PIL import Image
from collections import Counter
import json

app = Flask(__name__)

def get_top_colors(image_path, num_colors=10):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    pixel_count = Counter(pixels)
    top_colors = pixel_count.most_common(num_colors)
    return [f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}" for (c, _) in top_colors]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file provided."

    file = request.files['file']

    if file.filename == '':
        return "No file selected."

    if file:
        image_path = "D:/full stack development/pythonProject/cld92/uploads/pexels-photo-931177.jpeg"
        file.save(image_path)
        top_colors = get_top_colors(image_path)
        return json.dumps({"colors": top_colors})

if __name__ == '__main__':
    app.run(debug=True)
