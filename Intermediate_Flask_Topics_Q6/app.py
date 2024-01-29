from flask import Flask, render_template, request, redirect, url_for, send_from_directory

import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        try:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            print("Saving file to:", filename)
            file.save(filename)
            print("File saved successfully.")
            return redirect(url_for('uploaded_file', filename=file.filename))
        except Exception as e:
            print("Error uploading file:", str(e))
            return f"Error uploading file: {str(e)}"

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except Exception as e:
        return f"Error rendering template: {str(e)}"

@app.route('/list_files')
def list_files():
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return render_template('list_files.html', files=files)
    except Exception as e:
        return f"Error listing files: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
