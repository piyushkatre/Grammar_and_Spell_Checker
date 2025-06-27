from flask import Flask, render_template, request
from main import correct_spelling, correct_grammar
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    corrected_spelling = ""
    corrected_grammar = ""
    input_text = ""

    if request.method == 'POST':
        # Option 1: Text from textarea
        input_text = request.form.get('text', '')

        # Option 2: Text from uploaded file
        if 'file' in request.files:
            uploaded_file = request.files['file']
            if uploaded_file.filename.endswith('.txt'):
                input_text = uploaded_file.read().decode('utf-8')

        if input_text.strip() != "":
            corrected_spelling = correct_spelling(input_text)
            corrected_grammar = correct_grammar(corrected_spelling)

    return render_template("index.html", 
                           corrected_spelling=corrected_spelling,
                           corrected_grammar=corrected_grammar)

if __name__ == '__main__':
    app.run(debug=True)
