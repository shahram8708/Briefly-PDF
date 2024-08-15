from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import google.generativeai as genai
from werkzeug.utils import secure_filename
import PyPDF2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}
genai.configure(api_key=os.environ['API_KEY'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fullresponse')
def fullresponse():
    return render_template('fullresponse.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files or 'prompt' not in request.form:
        return jsonify({'error': 'No files or prompt provided'}), 400

    files = request.files.getlist('files[]')
    prompt = request.form['prompt']
    pdf_texts = []

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            pdf_texts.append(extract_text_from_pdf(file_path))

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt] + pdf_texts)
    
    response_text = response.text

    return jsonify({'response': response_text})

@app.route('/save/<filename>', methods=['GET'])
def save_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
